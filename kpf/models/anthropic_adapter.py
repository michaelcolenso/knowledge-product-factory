"""Anthropic Claude adapter."""

import anthropic
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from kpf.logger import get_logger

logger = get_logger("adapter.anthropic")

DEFAULT_MODEL = "claude-sonnet-4-6"


class AnthropicAdapter:
    """Anthropic Claude model adapter with retry logic."""

    def __init__(self, api_key: str, model: str = DEFAULT_MODEL) -> None:
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    @retry(
        wait=wait_exponential(multiplier=1, min=2, max=30),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type((anthropic.RateLimitError, anthropic.APIConnectionError)),
        reraise=True,
    )
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        response_format: str = "text",
    ) -> str:
        if response_format == "json":
            system_prompt = system_prompt + "\n\nIMPORTANT: You must respond with valid JSON only. No commentary, no markdown fences, no explanations outside the JSON object."

        response = self.client.messages.create(
            model=self.model,
            max_tokens=8192,
            temperature=temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )

        content = response.content[0]
        if hasattr(content, "text"):
            raw = content.text
        else:
            raw = str(content)

        logger.debug(
            f"Tokens used: input={response.usage.input_tokens}, output={response.usage.output_tokens}"
        )
        return raw
