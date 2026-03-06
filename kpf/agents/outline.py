from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.outline import Outline, OutlineSection
from kpf.utils.json_io import write_json


class OutlineAgent(BaseAgent):
    name = "outline"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        outline = Outline(
            title="Insurance Credentialing Accelerator",
            sections=[
                OutlineSection(title="Setup", bullets=["Entity prep", "NPI and CAQH setup"]),
                OutlineSection(title="Submission", bullets=["Payer packet assembly", "Follow-up cadence"]),
            ],
        )
        path = state.run_dir / "outline.json"
        write_json(path, outline.model_dump())
        state.data["outline"] = outline
        state.register_artifact("outline", path)
        return state
