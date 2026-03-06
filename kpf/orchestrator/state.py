from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from kpf.schemas.run_config import RunConfig


@dataclass
class OrchestratorState:
    config: RunConfig
    run_dir: Path
    data: dict[str, Any] = field(default_factory=dict)
    artifacts: dict[str, str] = field(default_factory=dict)
    gate_results: dict[str, bool] = field(default_factory=dict)

    def register_artifact(self, key: str, path: Path) -> None:
        self.artifacts[key] = str(path)

    def require(self, key: str) -> Any:
        if key not in self.data:
            raise RuntimeError(f"Missing upstream artifact in state: {key}")
        return self.data[key]
