"""SynthesisAgent - builds the knowledge base from all upstream research."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.knowledge_base import KnowledgeBase


class SynthesisAgent(BaseAgent):
    name = "synthesis"
    requires: list[str] = ["product_brief", "outline"]

    def _execute(self, state: PipelineState) -> PipelineState:
        context = (
            f"Niche: {state.niche}\n"
            f"Product brief: {state.artifacts['product_brief']}\n"
            f"Outline: {state.artifacts['outline']}\n"
            f"Pain map: {state.artifacts.get('pain_map', 'not available')}\n"
            f"Spending signals: {state.artifacts.get('spending_signals', 'not available')}\n"
            f"Competitor map: {state.artifacts.get('competitor_map', 'not available')}\n"
            f"Opportunity score: {state.artifacts.get('opportunity_score', 'not available')}"
        )

        raw = self.generate_structured(context, KnowledgeBase)
        kb = self.parse_with_repair(raw, KnowledgeBase)

        self.write_artifact("knowledge_base.json", kb, subdir="product")
        state.artifacts["knowledge_base"] = self.artifact_dict(kb)
        state.log(f"SynthesisAgent: {len(kb.facts)} facts synthesized")
        return state
