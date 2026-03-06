from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.utils.files import write_text


class DraftingAgent(BaseAgent):
    name = "drafting"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        outline = state.require("outline")
        lines = ["# Insurance Credentialing Accelerator", ""]
        for section in outline.sections:
            lines.append(f"## {section.title}")
            for bullet in section.bullets:
                lines.append(f"- {bullet}")
            lines.append("")
        content = "\n".join(lines)
        path = state.run_dir / "draft_product.md"
        write_text(path, content)
        state.data["draft_product"] = content
        state.register_artifact("draft_product", path)
        return state
