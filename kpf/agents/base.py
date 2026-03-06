from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
from pydantic import BaseModel

from kpf.models.mock_adapter import MockAdapter
from kpf.orchestrator.state import OrchestratorState


class BaseAgent(ABC):
    name: str

    def __init__(self) -> None:
        self.adapter = MockAdapter()

    def _prompt_dir(self) -> Path:
        return Path(__file__).resolve().parent.parent / "prompts" / self.name

    def _load_prompt(self, name: str) -> str:
        return (self._prompt_dir() / f"{name}.md").read_text(encoding="utf-8")

    def parse_with_repair(self, raw: str, schema: type[BaseModel]) -> BaseModel:
        try:
            return schema.model_validate_json(raw)
        except Exception:
            repaired = self.adapter.generate(
                self._load_prompt("validator"),
                raw,
            )
            return schema.model_validate_json(repaired)

    @abstractmethod
    def run(self, state: OrchestratorState) -> OrchestratorState:
        raise NotImplementedError
