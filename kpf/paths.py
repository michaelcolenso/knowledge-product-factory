"""Filesystem path constants and helpers for KPF."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
KPF_PACKAGE = Path(__file__).parent

RUNS_DIR = PROJECT_ROOT / "runs"
BRIEFS_DIR = PROJECT_ROOT / "briefs"
PRODUCTS_DIR = PROJECT_ROOT / "products"
PROMPTS_DIR = KPF_PACKAGE / "prompts"
MEMORY_DIR = KPF_PACKAGE / "memory"
TEMPLATES_DIR = KPF_PACKAGE / "templates"


def get_run_dir(run_id: str) -> Path:
    return RUNS_DIR / run_id


def get_prompt_path(agent_name: str, prompt_type: str) -> Path:
    return PROMPTS_DIR / agent_name / f"{prompt_type}.md"
