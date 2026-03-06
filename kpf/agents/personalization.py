"""PersonalizationAgent - defines personalization spec (optional)."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.personalization_spec import PersonalizationSpec


class PersonalizationAgent(BaseAgent):
    name = "personalization"
    requires: list[str] = ["product_brief", "draft_product"]

    def _execute(self, state: PipelineState) -> PipelineState:
        brief = state.artifacts["product_brief"]
        draft_excerpt = str(state.artifacts["draft_product"])[:2000]
        context = f"Product brief: {brief}\nDraft excerpt: {draft_excerpt}"

        raw = self.generate_structured(context, PersonalizationSpec)
        spec = self.parse_with_repair(raw, PersonalizationSpec)

        self.write_artifact("personalization_spec.json", spec, subdir="product")
        state.artifacts["personalization_spec"] = self.artifact_dict(spec)
        state.log(f"PersonalizationAgent: {len(spec.input_fields)} input fields defined")
        return state
