"""JSON read/write utilities using orjson."""

from pathlib import Path
from typing import Any

import orjson
from pydantic import BaseModel


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(orjson.dumps(data, option=orjson.OPT_INDENT_2))


def read_json(path: Path) -> dict[str, Any]:
    return orjson.loads(path.read_bytes())


def write_model(path: Path, model: BaseModel) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(orjson.dumps(model.model_dump(), option=orjson.OPT_INDENT_2))
