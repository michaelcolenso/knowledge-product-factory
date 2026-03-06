from pathlib import Path
from kpf.orchestrator.state import OrchestratorState
from kpf.utils.json_io import read_json, write_json


INDEX = Path("runs") / "index.json"


def append_run_record(state: OrchestratorState) -> None:
    records = []
    if INDEX.exists():
        records = read_json(INDEX)
    records.append(
        {
            "run_id": state.run_dir.name,
            "mode": state.config.mode,
            "niche": state.config.niche,
            "status": "completed",
            "artifact_paths": state.artifacts,
        }
    )
    write_json(INDEX, records)
