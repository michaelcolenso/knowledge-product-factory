"""Base agent class for all KPF agents."""

import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from kpf.logger import get_logger
from kpf.models.adapter_base import ModelAdapter
from kpf.orchestrator.state import PipelineState
from kpf.paths import get_prompt_path
from kpf.utils.json_io import write_model
from kpf.utils.text import extract_json_block
from kpf.utils.files import write_text


class BaseAgent(ABC):
    name: str
    requires: list[str] = []

    def __init__(self, adapter: ModelAdapter, run_dir: Path) -> None:
        self.adapter = adapter
        self.run_dir = run_dir
        self.logger = get_logger(f"agent.{self.name}")

    def run(self, state: PipelineState) -> PipelineState:
        self._check_prerequisites(state)
        self.logger.info(f"Starting {self.name}")
        result = self._execute(state)
        self.logger.info(f"Completed {self.name}")
        return result

    def _check_prerequisites(self, state: PipelineState) -> None:
        for key in self.requires:
            if key not in state.artifacts:
                raise RuntimeError(
                    f"{self.name} requires artifact '{key}' but it is missing from state"
                )

    @abstractmethod
    def _execute(self, state: PipelineState) -> PipelineState: ...

    def load_prompt(self, prompt_type: str) -> str:
        path = get_prompt_path(self.name, prompt_type)
        if not path.exists():
            return f"[Missing prompt: {path}]"
        return path.read_text(encoding="utf-8")

    def generate_structured(
        self,
        task_context: str,
        schema_class: type[BaseModel],
        temperature: float = 0.2,
    ) -> str:
        system = self.load_prompt("system")
        task = self.load_prompt("task")

        schema_json = json.dumps(schema_class.model_json_schema(), indent=2)
        task = task.replace("{schema_json}", schema_json)

        user = task + "\n\n" + task_context + f"\n\n<!-- schema_hint: {schema_class.__name__} -->"
        return self.adapter.generate(system, user, temperature, response_format="json")

    def parse_with_repair(self, raw: str, schema_class: type[BaseModel]) -> BaseModel:
        cleaned = extract_json_block(raw)
        try:
            return schema_class.model_validate_json(cleaned)
        except Exception as first_error:
            self.logger.warning(f"Parse failed, attempting repair: {first_error}")
            repaired = self._repair(cleaned, schema_class)
            return schema_class.model_validate_json(repaired)

    def _repair(self, raw: str, schema_class: type[BaseModel]) -> str:
        validator_prompt = self.load_prompt("validator")
        schema_json = json.dumps(schema_class.model_json_schema(), indent=2)
        validator_prompt = validator_prompt.replace("{schema_json}", schema_json)
        return self.adapter.generate(
            "You are a JSON repair assistant.",
            validator_prompt + "\n\nBroken JSON:\n" + raw,
            temperature=0.0,
        )

    def write_artifact(
        self,
        filename: str,
        data: BaseModel | str,
        subdir: str = "",
    ) -> Path:
        target_dir = self.run_dir / subdir if subdir else self.run_dir
        target_dir.mkdir(parents=True, exist_ok=True)
        path = target_dir / filename
        if isinstance(data, str):
            write_text(path, data)
        else:
            write_model(path, data)
        return path

    def artifact_dict(self, model: BaseModel) -> dict[str, Any]:
        return model.model_dump()
