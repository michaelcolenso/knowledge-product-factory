from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    model_provider: str = os.getenv("KPF_MODEL_PROVIDER", "mock")
    model_name: str = os.getenv("KPF_MODEL_NAME", "mock-kpf-v1")
    runs_dir: str = os.getenv("KPF_RUNS_DIR", "runs")
    briefs_dir: str = os.getenv("KPF_BRIEFS_DIR", "briefs")
    products_dir: str = os.getenv("KPF_PRODUCTS_DIR", "products")
    memory_dir: str = os.getenv("KPF_MEMORY_DIR", "kpf/memory")
    min_spending_signals: int = int(os.getenv("KPF_MIN_SPENDING_SIGNALS", "2"))
    min_pain_points: int = int(os.getenv("KPF_MIN_PAIN_POINTS", "2"))
    min_score: int = int(os.getenv("KPF_MIN_SCORE", "18"))


settings = Settings()
