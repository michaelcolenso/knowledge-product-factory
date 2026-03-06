"""Structured logging for KPF."""

import logging

from rich.logging import RichHandler


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = RichHandler(
            show_path=False,
            markup=True,
            rich_tracebacks=True,
        )
        logger.addHandler(handler)
        logger.propagate = False
    return logger


def configure_root_logger(level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(message)s",
        datefmt="[%X]",
        handlers=[
            RichHandler(
                show_path=False,
                markup=True,
                rich_tracebacks=True,
            )
        ],
    )
