"""DraftingAgent - produces long-form markdown product draft."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState


class DraftingAgent(BaseAgent):
    name = "drafting"
    requires: list[str] = ["outline", "knowledge_base", "product_brief"]

    def _execute(self, state: PipelineState) -> PipelineState:
        system = self.load_prompt("system")
        task = self.load_prompt("task")

        outline = state.artifacts["outline"]
        kb = state.artifacts["knowledge_base"]
        brief = state.artifacts["product_brief"]

        user = (
            task
            + f"\n\nProduct Brief:\n{brief}"
            + f"\n\nOutline:\n{outline}"
            + f"\n\nKnowledge Base:\n{kb}"
        )

        # Drafting returns markdown, not JSON
        draft_md = self.adapter.generate(system, user, temperature=0.4, response_format="text")

        self.write_artifact("draft_product.md", draft_md, subdir="product")
        state.artifacts["draft_product"] = draft_md
        state.log(f"DraftingAgent: draft written ({len(draft_md)} chars)")
        return state
