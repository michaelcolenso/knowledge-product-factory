"""Markdown helpers."""

from pathlib import Path


def write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def section_header(title: str, level: int = 2) -> str:
    return "#" * level + " " + title
