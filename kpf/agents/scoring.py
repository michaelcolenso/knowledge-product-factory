"""ScoringAgent - scores the opportunity across 5 dimensions."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.opportunity_score import OpportunityScore


class ScoringAgent(BaseAgent):
    name = "scoring"
    requires: list[str] = ["spending_signals", "pain_map", "competitor_map"]

    def _execute(self, state: PipelineState) -> PipelineState:
        context = (
            f"Spending signals: {state.artifacts['spending_signals']}\n"
            f"Pain map: {state.artifacts['pain_map']}\n"
            f"Competitor map: {state.artifacts['competitor_map']}"
        )

        raw = self.generate_structured(context, OpportunityScore)
        score = self.parse_with_repair(raw, OpportunityScore)

        self.write_artifact("opportunity_score.json", score, subdir="niche_analysis")
        state.artifacts["opportunity_score"] = self.artifact_dict(score)
        state.log(f"ScoringAgent: total={score.total}, decision={score.decision}")
        return state
