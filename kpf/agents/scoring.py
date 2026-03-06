from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.opportunity_score import OpportunityScore
from kpf.utils.json_io import write_json


class ScoringAgent(BaseAgent):
    name = "scoring"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        score = OpportunityScore(
            niche=state.config.niche or "unknown",
            spending_score=8,
            pain_score=8,
            competition_score=5,
            total_score=21,
            rationale="Clear spending, painful bottleneck, and room for a structured DIY product.",
        )
        path = state.run_dir / "opportunity_score.json"
        write_json(path, score.model_dump())
        state.data["opportunity_score"] = score
        state.register_artifact("opportunity_score", path)
        return state
