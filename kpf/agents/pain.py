"""PainAgent - maps pain patterns for the niche."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.pain_map import PainMap


class PainAgent(BaseAgent):
    name = "pain"
    requires: list[str] = ["run_config", "spending_signals"]

    def _execute(self, state: PipelineState) -> PipelineState:
        niche = state.niche or "general knowledge products"
        spending = state.artifacts["spending_signals"]
        context = f"Niche: {niche}\nSpending signals: {spending}"

        raw = self.generate_structured(context, PainMap)
        pain = self.parse_with_repair(raw, PainMap)

        self.write_artifact("pain_map.json", pain, subdir="niche_analysis")
        state.artifacts["pain_map"] = self.artifact_dict(pain)
        state.log(f"PainAgent: {len(pain.patterns)} pain patterns identified")
        return state
