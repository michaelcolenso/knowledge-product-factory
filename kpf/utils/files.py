"""File system helpers."""

from pathlib import Path

from kpf.utils.dates import today_str
from kpf.utils.slug import slugify


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def make_run_id(niche: str | None = None) -> str:
    date_part = today_str()
    if niche:
        slug = slugify(niche)
        return f"{date_part}_{slug}"
    return f"{date_part}_discovery"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
