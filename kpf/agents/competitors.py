"""CompetitorsAgent - maps competitive landscape for the niche."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.competitor_map import CompetitorMap


class CompetitorsAgent(BaseAgent):
    name = "competitors"
    requires: list[str] = ["run_config", "pain_map"]

    def _execute(self, state: PipelineState) -> PipelineState:
        niche = state.niche or "general knowledge products"
        pain = state.artifacts["pain_map"]
        context = f"Niche: {niche}\nPain map: {pain}"

        raw = self.generate_structured(context, CompetitorMap)
        competitor_map = self.parse_with_repair(raw, CompetitorMap)

        self.write_artifact("competitor_map.json", competitor_map, subdir="niche_analysis")
        state.artifacts["competitor_map"] = self.artifact_dict(competitor_map)
        state.log(f"CompetitorsAgent: {len(competitor_map.alternatives)} alternatives mapped")
        return state
