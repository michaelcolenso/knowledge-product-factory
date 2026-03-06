"""IntakeAgent - normalizes CLI inputs into RunConfig and creates run directory."""

from pathlib import Path

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.run_config import RunConfig
from kpf.utils.json_io import write_model


class IntakeAgent(BaseAgent):
    name = "intake"
    requires: list[str] = []

    def _execute(self, state: PipelineState) -> PipelineState:
        config = RunConfig(
            mode=state.mode,
            niche=state.niche,
        )

        if state.config:
            if "max_weeks" in state.config:
                config.constraints.max_creation_weeks = state.config["max_weeks"]
            if "price_floor" in state.config:
                config.constraints.price_floor = state.config["price_floor"]
            if "price_ceiling" in state.config:
                config.constraints.price_ceiling = state.config["price_ceiling"]
            if "formats" in state.config:
                config.constraints.allowed_formats = state.config["formats"]
            if "with_personalization" in state.config:
                config.with_personalization = state.config["with_personalization"]
            if "strict" in state.config:
                config.strict_mode = state.config["strict"]

        assert state.run_dir is not None
        write_model(state.run_dir / "run_config.json", config)

        state.artifacts["run_config"] = config.model_dump()
        state.log(f"IntakeAgent: run_config written to {state.run_dir}/run_config.json")
        return state
