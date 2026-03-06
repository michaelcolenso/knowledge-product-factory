"""OpenAI adapter (placeholder)."""


class OpenAIAdapter:
    """OpenAI model adapter - not yet implemented."""

    def __init__(self, api_key: str, model: str = "gpt-4o") -> None:
        self.api_key = api_key
        self.model = model

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        response_format: str = "text",
    ) -> str:
        raise NotImplementedError("OpenAI adapter not yet implemented. Use --model anthropic or --model mock.")
