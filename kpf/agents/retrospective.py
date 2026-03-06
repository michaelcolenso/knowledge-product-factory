from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.storage.memory_store import record
from kpf.settings import settings
from kpf.utils.json_io import write_json
from pathlib import Path


class RetrospectiveAgent(BaseAgent):
    name = "retrospective"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        report = {
            "niche": state.config.niche,
            "score": state.data.get("opportunity_score").total_score if state.data.get("opportunity_score") else None,
            "notes": ["Run completed", "Capture feedback before next iteration"],
        }
        path = state.run_dir / "retrospective.json"
        write_json(path, report)
        state.data["retrospective"] = report
        state.register_artifact("retrospective", path)
        memory_root = Path(settings.memory_dir)
        target = "winning_niches.json" if report.get("score", 0) and report["score"] >= 18 else "failed_niches.json"
        record(memory_root, target, {"niche": state.config.niche, "run_id": state.run_dir.name})
        return state
