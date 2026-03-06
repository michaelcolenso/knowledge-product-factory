"""SpendingAgent - synthesizes spending signals for the niche."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.spending_signal import SpendingSignalsReport


class SpendingAgent(BaseAgent):
    name = "spending"
    requires: list[str] = ["run_config"]

    def _execute(self, state: PipelineState) -> PipelineState:
        niche = state.niche or "general knowledge products"
        context = f"Niche: {niche}"
        if "niche_candidates" in state.artifacts:
            context += f"\nNiche candidates: {state.artifacts['niche_candidates']}"

        raw = self.generate_structured(context, SpendingSignalsReport)
        report = self.parse_with_repair(raw, SpendingSignalsReport)

        self.write_artifact("spending_signals.json", report, subdir="niche_analysis")
        state.artifacts["spending_signals"] = self.artifact_dict(report)
        state.log(f"SpendingAgent: {report.signal_count} signals found, passes={report.passes_threshold}")
        return state
