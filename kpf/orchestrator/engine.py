from __future__ import annotations
from pathlib import Path
from kpf.orchestrator.state import OrchestratorState
from kpf.paths import create_run_dir
from kpf.schemas.run_config import RunConfig
from kpf.storage.run_store import append_run_record
from kpf.orchestrator.gates import enforce_gate
from kpf.orchestrator.router import get_agent
from kpf.utils.json_io import write_json


def initialize_state(config: RunConfig) -> OrchestratorState:
    run_dir = create_run_dir(config.mode, config.niche)
    state = OrchestratorState(config=config, run_dir=run_dir)
    write_json(run_dir / "run_config.json", config.model_dump())
    state.register_artifact("run_config", run_dir / "run_config.json")
    return state


def _run(name: str, state: OrchestratorState) -> OrchestratorState:
    return get_agent(name)().run(state)


def run_pipeline(config: RunConfig) -> OrchestratorState:
    state = initialize_state(config)
    state = _run("intake", state)

    if not config.niche and config.mode in {"discover", "full"}:
        state = _run("discovery", state)
        if config.mode == "discover":
            append_run_record(state)
            return state

    should_run_research = config.mode in {"validate", "full"} or (
        config.mode == "build" and not config.brief
    )
    if should_run_research:
        state = _run("spending", state)
        enforce_gate("spending", state)
        state = _run("pain", state)
        enforce_gate("pain", state)
        state = _run("competitors", state)
        state = _run("scoring", state)
        enforce_gate("score", state)
        if config.mode == "validate":
            append_run_record(state)
            return state

    should_run_build = config.mode in {"build", "full"} or (
        config.mode == "launch" and not config.product
    )
    if should_run_build:
        state = _run("strategy", state)
        state = _run("outline", state)
        state = _run("synthesis", state)
        state = _run("drafting", state)
        state = _run("artifacts", state)
        if config.with_personalization:
            state = _run("personalization", state)
        state = _run("packaging", state)
        state = _run("validation", state)
        enforce_gate("validation", state)
        if config.mode == "build":
            append_run_record(state)
            return state

    if config.mode in {"launch", "full"}:
        state = _run("launch", state)
        state = _run("retrospective", state)

    append_run_record(state)
    return state
