"""Gemini adapter (placeholder)."""


class GeminiAdapter:
    """Google Gemini model adapter - not yet implemented."""

    def __init__(self, api_key: str, model: str = "gemini-1.5-pro") -> None:
        self.api_key = api_key
        self.model = model

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        response_format: str = "text",
    ) -> str:
        raise NotImplementedError("Gemini adapter not yet implemented. Use --model anthropic or --model mock.")
