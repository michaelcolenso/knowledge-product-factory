from kpf.settings import settings


def load_config() -> dict:
    return settings.__dict__.copy()
