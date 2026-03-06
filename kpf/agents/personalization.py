from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.personalization_spec import PersonalizationSpec
from kpf.utils.json_io import write_json


class PersonalizationAgent(BaseAgent):
    name = "personalization"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        spec = PersonalizationSpec(
            variables=["state", "payer_mix", "license_type"],
            instructions=["Swap payer names", "Adjust timelines by state", "Tailor submission checklist"],
        )
        path = state.run_dir / "personalization_spec.json"
        write_json(path, spec.model_dump())
        state.data["personalization_spec"] = spec
        state.register_artifact("personalization_spec", path)
        return state
