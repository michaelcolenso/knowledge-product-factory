from typing import Protocol


class ModelAdapter(Protocol):
    def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str: ...
