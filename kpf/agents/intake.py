from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.utils.json_io import write_json


class IntakeAgent(BaseAgent):
    name = "intake"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        niche = state.config.niche or ""
        payload = {"mode": state.config.mode, "niche": niche, "max_weeks": state.config.max_weeks}
        path = state.run_dir / "intake.json"
        write_json(path, payload)
        state.data["intake"] = payload
        state.register_artifact("intake", path)
        return state
