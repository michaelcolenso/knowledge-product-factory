from typing import Literal
from pydantic import BaseModel, Field


class RunConfig(BaseModel):
    mode: Literal["discover", "validate", "build", "launch", "full"]
    niche: str | None = None
    brief: str | None = None
    product: str | None = None
    max_weeks: int = Field(default=3, ge=1, le=8)
    min_score: int = 18
    with_personalization: bool = False
    model_provider: str = "mock"
