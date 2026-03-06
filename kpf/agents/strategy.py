"""StrategyAgent - builds the product brief from validated opportunity data."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.product_brief import ProductBrief


class StrategyAgent(BaseAgent):
    name = "strategy"
    requires: list[str] = ["opportunity_score", "pain_map", "competitor_map"]

    def _execute(self, state: PipelineState) -> PipelineState:
        context = (
            f"Niche: {state.niche}\n"
            f"Opportunity score: {state.artifacts['opportunity_score']}\n"
            f"Pain map: {state.artifacts['pain_map']}\n"
            f"Competitor map: {state.artifacts['competitor_map']}"
        )
        if "spending_signals" in state.artifacts:
            context += f"\nSpending signals: {state.artifacts['spending_signals']}"
        if "run_config" in state.artifacts:
            context += f"\nConstraints: {state.artifacts['run_config']}"

        raw = self.generate_structured(context, ProductBrief)
        brief = self.parse_with_repair(raw, ProductBrief)

        self.write_artifact("product_brief.json", brief, subdir="product")
        state.artifacts["product_brief"] = self.artifact_dict(brief)
        state.log(f"StrategyAgent: product brief created - {brief.opportunity_name}")
        return state
