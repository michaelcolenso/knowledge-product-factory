"""OutlineAgent - creates the section-level outline for the product."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.outline import Outline


class OutlineAgent(BaseAgent):
    name = "outline"
    requires: list[str] = ["product_brief"]

    def _execute(self, state: PipelineState) -> PipelineState:
        context = (
            f"Product brief: {state.artifacts['product_brief']}\n"
            f"Pain map: {state.artifacts.get('pain_map', 'not available')}"
        )

        raw = self.generate_structured(context, Outline)
        outline = self.parse_with_repair(raw, Outline)

        self.write_artifact("outline.json", outline, subdir="product")
        state.artifacts["outline"] = self.artifact_dict(outline)
        state.log(f"OutlineAgent: {len(outline.sections)} sections outlined")
        return state
