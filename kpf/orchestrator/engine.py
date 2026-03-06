"""Pipeline engine - orchestrates agents in sequence."""

from pathlib import Path

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from kpf.logger import get_logger
from kpf.models.adapter_base import ModelAdapter
from kpf.orchestrator.gates import (
    GateError,
    enforce_artifact_gate,
    enforce_launch_gate,
    enforce_pain_gate,
    enforce_score_gate,
    enforce_spending_gate,
)
from kpf.orchestrator.router import (
    should_run_build,
    should_run_discovery,
    should_run_launch,
    should_run_personalization,
    should_run_validation,
    stop_after_build,
    stop_after_discovery,
    stop_after_validation,
)
from kpf.orchestrator.state import PipelineState
from kpf.schemas.run_config import RunConfig
from kpf.utils.files import make_run_id
from kpf.utils.json_io import write_json
from kpf.paths import RUNS_DIR

logger = get_logger("engine")
console = Console()


class PipelineEngine:
    def run(self, config: RunConfig, adapter: ModelAdapter) -> PipelineState:
        run_id = make_run_id(config.niche)
        run_dir = RUNS_DIR / run_id
        run_dir.mkdir(parents=True, exist_ok=True)

        state = PipelineState(
            run_id=run_id,
            mode=config.mode,
            niche=config.niche,
            run_dir=run_dir,
        )

        try:
            state = self._run_pipeline(state, config, adapter)
        except GateError as e:
            console.print(f"\n[bold red]Gate Blocked:[/bold red] [{e.gate}] {e.reason}")
            state.log(f"GATE_FAIL: {e.gate} - {e.reason}")
            state.gates[e.gate] = False
        except Exception as e:
            console.print(f"\n[bold red]Pipeline Error:[/bold red] {e}")
            logger.exception("Unexpected pipeline error")
            raise
        finally:
            self._write_summary(state)

        return state

    def _run_pipeline(
        self, state: PipelineState, config: RunConfig, adapter: ModelAdapter
    ) -> PipelineState:
        from kpf.agents.intake import IntakeAgent
        from kpf.agents.discovery import DiscoveryAgent
        from kpf.agents.spending import SpendingAgent
        from kpf.agents.pain import PainAgent
        from kpf.agents.competitors import CompetitorsAgent
        from kpf.agents.scoring import ScoringAgent
        from kpf.agents.strategy import StrategyAgent
        from kpf.agents.outline import OutlineAgent
        from kpf.agents.synthesis import SynthesisAgent
        from kpf.agents.drafting import DraftingAgent
        from kpf.agents.artifacts import ArtifactsAgent
        from kpf.agents.personalization import PersonalizationAgent
        from kpf.agents.packaging import PackagingAgent
        from kpf.agents.validation import ValidationAgent
        from kpf.agents.launch import LaunchAgent
        from kpf.agents.retrospective import RetrospectiveAgent

        assert state.run_dir is not None

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True,
        ) as progress:

            def run_agent(agent_class: type, label: str) -> PipelineState:
                task = progress.add_task(f"[cyan]{label}...", total=None)
                agent = agent_class(adapter=adapter, run_dir=state.run_dir)
                result = agent.run(state)
                progress.remove_task(task)
                return result

            # Intake always runs
            state = run_agent(IntakeAgent, "Intake")

            # Discovery phase
            if should_run_discovery(config):
                state = run_agent(DiscoveryAgent, "Discovery")
                if stop_after_discovery(config):
                    return state

            # Validation phase
            if should_run_validation(config):
                state = run_agent(SpendingAgent, "Spending Analysis")
                enforce_spending_gate(state)

                state = run_agent(PainAgent, "Pain Mapping")
                enforce_pain_gate(state)

                state = run_agent(CompetitorsAgent, "Competitor Analysis")
                state = run_agent(ScoringAgent, "Opportunity Scoring")
                enforce_score_gate(state)

                if stop_after_validation(config):
                    return state

            # Build phase
            if should_run_build(config):
                state = run_agent(StrategyAgent, "Strategy")
                state = run_agent(OutlineAgent, "Outline")
                state = run_agent(SynthesisAgent, "Synthesis")
                state = run_agent(DraftingAgent, "Drafting")
                state = run_agent(ArtifactsAgent, "Artifacts")

                if should_run_personalization(config):
                    state = run_agent(PersonalizationAgent, "Personalization")

                state = run_agent(PackagingAgent, "Packaging")
                state = run_agent(ValidationAgent, "Validation")
                enforce_artifact_gate(state)

                if stop_after_build(config):
                    return state

            # Launch phase
            if should_run_launch(config):
                enforce_launch_gate(state)
                state = run_agent(LaunchAgent, "Launch Assets")
                state = run_agent(RetrospectiveAgent, "Retrospective")

        return state

    def _write_summary(self, state: PipelineState) -> None:
        if state.run_dir is None:
            return
        summary = {
            "run_id": state.run_id,
            "mode": state.mode,
            "niche": state.niche,
            "artifact_keys": list(state.artifacts.keys()),
            "gates": state.gates,
            "log_count": len(state.logs),
        }
        write_json(state.run_dir / "summary.json", summary)
