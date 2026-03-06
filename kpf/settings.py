"""Application settings loaded from environment variables."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="KPF_",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    anthropic_api_key: str = ""
    openai_api_key: str = ""
    default_model: str = "anthropic"
    log_level: str = "INFO"
    cache_responses: bool = False


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
