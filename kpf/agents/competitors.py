from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.competitor_map import CompetitorMap, Competitor
from kpf.utils.json_io import write_json


class CompetitorsAgent(BaseAgent):
    name = "competitors"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        niche = state.config.niche or "unknown"
        cmap = CompetitorMap(
            niche=niche,
            competitors=[
                Competitor(name="Agency A", offer="Done-for-you credentialing", price="$1500", gap="No DIY system"),
                Competitor(name="Template Shop B", offer="Single checklist", price="$49", gap="Not end-to-end"),
            ],
        )
        path = state.run_dir / "competitor_map.json"
        write_json(path, cmap.model_dump())
        state.data["competitor_map"] = cmap
        state.register_artifact("competitor_map", path)
        return state
