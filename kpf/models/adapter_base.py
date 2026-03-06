"""Base protocol for model adapters."""

from typing import Protocol, runtime_checkable


@runtime_checkable
class ModelAdapter(Protocol):
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        response_format: str = "text",
    ) -> str:
        """Generate a response from the model.

        Args:
            system_prompt: The system/role prompt.
            user_prompt: The user task prompt.
            temperature: Sampling temperature (0.0 to 1.0).
            response_format: "text" for free text, "json" for structured JSON output.

        Returns:
            The model's response as a string.
        """
        ...
