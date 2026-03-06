import json
from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.niche_candidate import DiscoveryReport
from kpf.utils.json_io import write_json


class DiscoveryAgent(BaseAgent):
    name = "discovery"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        raw = self.adapter.generate(self._load_prompt("system"), self._load_prompt("task"))
        report = self.parse_with_repair(raw, DiscoveryReport)
        if not state.config.niche and report.niches:
            state.config.niche = report.niches[0].name
        path = state.run_dir / "discovery_report.json"
        write_json(path, json.loads(report.model_dump_json()))
        state.data["discovery_report"] = report
        state.register_artifact("discovery_report", path)
        return state
