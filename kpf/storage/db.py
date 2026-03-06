"""SQLite database setup."""

from pathlib import Path

from sqlmodel import SQLModel, create_engine

from kpf.paths import RUNS_DIR

DB_PATH = RUNS_DIR / ".kpf.db"
_engine = None


def get_engine():
    global _engine
    if _engine is None:
        RUNS_DIR.mkdir(parents=True, exist_ok=True)
        _engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
    return _engine


def create_tables() -> None:
    SQLModel.metadata.create_all(get_engine())
