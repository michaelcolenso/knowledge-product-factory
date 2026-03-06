"""Model adapter factory."""

from kpf.models.adapter_base import ModelAdapter
from kpf.models.anthropic_adapter import AnthropicAdapter
from kpf.models.gemini_adapter import GeminiAdapter
from kpf.models.mock_adapter import MockAdapter
from kpf.models.openai_adapter import OpenAIAdapter
from kpf.settings import Settings


def get_adapter(model_name: str, settings: Settings) -> ModelAdapter:
    match model_name:
        case "anthropic":
            return AnthropicAdapter(api_key=settings.anthropic_api_key)
        case "openai":
            return OpenAIAdapter(api_key=settings.openai_api_key)
        case "gemini":
            return GeminiAdapter(api_key="")
        case "mock":
            return MockAdapter()
        case _:
            raise ValueError(f"Unknown model adapter: {model_name!r}. Supported: anthropic, openai, gemini, mock")


__all__ = [
    "ModelAdapter",
    "AnthropicAdapter",
    "GeminiAdapter",
    "MockAdapter",
    "OpenAIAdapter",
    "get_adapter",
]
