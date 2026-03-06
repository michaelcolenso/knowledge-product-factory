"""RetrospectiveAgent - records postmortem and updates memory files."""

import json
from pathlib import Path

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.paths import MEMORY_DIR
from kpf.utils.dates import today_str
from kpf.utils.json_io import read_json, write_json


class RetrospectiveAgent(BaseAgent):
    name = "retrospective"
    requires: list[str] = ["opportunity_score", "validation_report"]

    def _execute(self, state: PipelineState) -> PipelineState:
        score = state.artifacts["opportunity_score"]
        validation = state.artifacts["validation_report"]
        brief = state.artifacts.get("product_brief", {})

        postmortem = {
            "run_id": state.run_id,
            "niche": state.niche,
            "date": today_str(),
            "opportunity_score": score.get("total"),
            "decision": score.get("decision"),
            "validation_status": validation.get("status"),
            "format_used": brief.get("format"),
            "gates_passed": state.gates,
            "log_entries": len(state.logs),
        }

        self.write_artifact("postmortem.json", postmortem if False else _dict_to_model(postmortem))
        # Write as raw dict since postmortem has no schema
        import orjson
        postmortem_path = self.run_dir / "postmortem.json"
        postmortem_path.write_bytes(orjson.dumps(postmortem, option=orjson.OPT_INDENT_2))

        self._update_memory(state, postmortem, validation, score, brief)

        state.artifacts["postmortem"] = postmortem
        state.log("RetrospectiveAgent: postmortem written and memory updated")
        return state

    def _update_memory(
        self,
        state: PipelineState,
        postmortem: dict,
        validation: dict,
        score: dict,
        brief: dict,
    ) -> None:
        MEMORY_DIR.mkdir(parents=True, exist_ok=True)

        if validation.get("status") == "PASS":
            self._append_to_memory(
                MEMORY_DIR / "winning_niches.json",
                "niches",
                {
                    "niche": state.niche,
                    "score": score.get("total"),
                    "format": brief.get("format"),
                    "date": today_str(),
                },
            )
        else:
            self._append_to_memory(
                MEMORY_DIR / "failed_niches.json",
                "niches",
                {
                    "niche": state.niche,
                    "score": score.get("total"),
                    "reason": validation.get("status"),
                    "date": today_str(),
                },
            )

        fmt = brief.get("format")
        if fmt:
            perf_path = MEMORY_DIR / "format_performance.json"
            perf = read_json(perf_path) if perf_path.exists() else {"formats": {}}
            if fmt not in perf["formats"]:
                perf["formats"][fmt] = {"runs": 0, "passes": 0}
            perf["formats"][fmt]["runs"] += 1
            if validation.get("status") == "PASS":
                perf["formats"][fmt]["passes"] += 1
            write_json(perf_path, perf)

    def _append_to_memory(self, path: Path, key: str, entry: dict) -> None:
        data = read_json(path) if path.exists() else {key: []}
        data[key].append(entry)
        write_json(path, data)


def _dict_to_model(d: dict):
    from pydantic import BaseModel
    class _Stub(BaseModel):
        pass
    return d
