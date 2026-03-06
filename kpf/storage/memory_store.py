from pathlib import Path
from kpf.utils.json_io import read_json, write_json


DEFAULT_FILES = [
    "winning_niches.json",
    "failed_niches.json",
    "search_patterns.json",
    "format_performance.json",
]


def initialize_memory(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    for f in DEFAULT_FILES:
        p = root / f
        if not p.exists():
            write_json(p, [])


def record(root: Path, filename: str, item: dict) -> None:
    path = root / filename
    data = read_json(path) if path.exists() else []
    data.append(item)
    write_json(path, data)
