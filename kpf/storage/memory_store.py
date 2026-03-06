"""JSON-based memory store for niches and performance data."""

from pathlib import Path

from kpf.paths import MEMORY_DIR
from kpf.utils.dates import today_str
from kpf.utils.json_io import read_json, write_json


class MemoryStore:
    def __init__(self, memory_dir: Path = MEMORY_DIR) -> None:
        self.memory_dir = memory_dir
        self.memory_dir.mkdir(parents=True, exist_ok=True)

    def add_winning_niche(self, niche: str, score: int, format_used: str = "") -> None:
        path = self.memory_dir / "winning_niches.json"
        data = read_json(path) if path.exists() else {"niches": []}
        data["niches"].append({
            "niche": niche,
            "score": score,
            "format": format_used,
            "date": today_str(),
        })
        write_json(path, data)

    def add_failed_niche(self, niche: str, reason: str) -> None:
        path = self.memory_dir / "failed_niches.json"
        data = read_json(path) if path.exists() else {"niches": []}
        data["niches"].append({
            "niche": niche,
            "reason": reason,
            "date": today_str(),
        })
        write_json(path, data)

    def get_winning_niches(self) -> list[dict]:
        path = self.memory_dir / "winning_niches.json"
        return read_json(path).get("niches", []) if path.exists() else []

    def get_failed_niches(self) -> list[dict]:
        path = self.memory_dir / "failed_niches.json"
        return read_json(path).get("niches", []) if path.exists() else []
