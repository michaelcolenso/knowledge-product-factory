from datetime import datetime
from pathlib import Path
from kpf.settings import settings


def ensure_path(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_runs_root() -> Path:
    return ensure_path(Path(settings.runs_dir))


def create_run_dir(mode: str, niche: str | None = None) -> Path:
    slug = (niche or mode).lower().replace(" ", "_").replace("/", "_")[:40]
    stamp = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    return ensure_path(get_runs_root() / f"{stamp}_{slug}")
