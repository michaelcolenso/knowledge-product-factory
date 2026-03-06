"""Artifact path registry for runs."""

from pathlib import Path


class ArtifactStore:
    """Tracks artifact file paths for a run."""

    def __init__(self) -> None:
        self._registry: dict[str, dict[str, Path]] = {}

    def register(self, run_id: str, key: str, path: Path) -> None:
        if run_id not in self._registry:
            self._registry[run_id] = {}
        self._registry[run_id][key] = path

    def get_path(self, run_id: str, key: str) -> Path | None:
        return self._registry.get(run_id, {}).get(key)

    def list_keys(self, run_id: str) -> list[str]:
        return list(self._registry.get(run_id, {}).keys())
