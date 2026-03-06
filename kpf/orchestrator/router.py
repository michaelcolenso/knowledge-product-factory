"""Routing logic for the KPF pipeline."""

from kpf.schemas.run_config import RunConfig


def should_run_discovery(config: RunConfig) -> bool:
    return config.niche is None and config.mode in {"discover", "full"}


def should_run_validation(config: RunConfig) -> bool:
    return config.mode in {"validate", "full"}


def should_run_build(config: RunConfig) -> bool:
    return config.mode in {"build", "full"}


def should_run_launch(config: RunConfig) -> bool:
    return config.mode in {"launch", "full"}


def should_run_personalization(config: RunConfig) -> bool:
    from kpf.config import PERSONALIZATION_ELIGIBLE_FORMATS
    return config.with_personalization


def stop_after_discovery(config: RunConfig) -> bool:
    return config.mode == "discover"


def stop_after_validation(config: RunConfig) -> bool:
    return config.mode == "validate"


def stop_after_build(config: RunConfig) -> bool:
    return config.mode == "build"
