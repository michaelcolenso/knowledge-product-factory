from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.pain_map import PainMap, PainPoint
from kpf.utils.json_io import write_json


class PainAgent(BaseAgent):
    name = "pain"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        niche = state.config.niche or "unknown"
        report = PainMap(
            niche=niche,
            pains=[
                PainPoint(pain="Long insurer enrollment cycles", specificity="90-120 day delays", urgency=5),
                PainPoint(pain="Denied claims due to setup mistakes", specificity="NPI/taxonomy mismatches", urgency=4),
            ],
        )
        path = state.run_dir / "pain_map.json"
        write_json(path, report.model_dump())
        state.data["pain_map"] = report
        state.register_artifact("pain_map", path)
        return state
