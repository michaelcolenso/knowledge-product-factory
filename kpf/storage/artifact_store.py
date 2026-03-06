from pathlib import Path


def artifact_path(run_dir: Path, relative: str) -> Path:
    path = run_dir / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
