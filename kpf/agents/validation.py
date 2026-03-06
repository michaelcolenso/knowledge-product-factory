from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.validation_report import ValidationReport
from kpf.utils.json_io import write_json


class ValidationAgent(BaseAgent):
    name = "validation"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        required = ["product_brief", "outline", "draft_product", "artifact_manifest", "package_manifest"]
        missing = [k for k in required if k not in state.data]
        report = ValidationReport(
            gate_results={"artifacts_present": not missing},
            ready_to_ship=not missing,
            notes=[] if not missing else [f"Missing: {', '.join(missing)}"],
        )
        path = state.run_dir / "validation_report.json"
        write_json(path, report.model_dump())
        state.data["validation_report"] = report
        state.register_artifact("validation_report", path)
        return state
