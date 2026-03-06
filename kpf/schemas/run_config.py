"""RunConfig schema."""

from typing import Literal

from pydantic import BaseModel, Field


class Constraints(BaseModel):
    max_creation_weeks: int = Field(default=3, description="Maximum weeks allowed for product creation")
    allowed_formats: list[str] = Field(
        default=["playbook", "template_library", "notion_system"],
        description="Permitted product formats",
    )
    price_floor: int = Field(default=79, description="Minimum product price in USD")
    price_ceiling: int = Field(default=199, description="Maximum product price in USD")


class RunConfig(BaseModel):
    mode: Literal["discover", "validate", "build", "launch", "full"] = Field(
        description="Pipeline execution mode"
    )
    niche: str | None = Field(default=None, description="Target niche to evaluate")
    target_audience: str | None = Field(default=None, description="Specific audience segment")
    constraints: Constraints = Field(default_factory=Constraints, description="Product constraints")
    strict_mode: bool = Field(default=True, description="Enforce all gates strictly")
    with_personalization: bool = Field(default=False, description="Include personalization agent")
    model: str = Field(default="anthropic", description="Model adapter to use")
    temperature: float = Field(default=0.2, description="LLM temperature setting")
    output_dir: str | None = Field(default=None, description="Override output directory")
