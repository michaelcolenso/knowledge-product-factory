"""Pipeline state dataclass."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class PipelineState:
    run_id: str
    mode: str
    niche: str | None
    artifacts: dict[str, Any] = field(default_factory=dict)
    config: dict[str, Any] = field(default_factory=dict)
    logs: list[str] = field(default_factory=list)
    gates: dict[str, bool] = field(default_factory=dict)
    run_dir: Path | None = None

    def log(self, message: str) -> None:
        self.logs.append(message)
