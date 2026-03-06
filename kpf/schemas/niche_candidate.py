"""NicheCandidate schema."""

from typing import Literal

from pydantic import BaseModel, Field


class NicheCandidate(BaseModel):
    niche_name: str = Field(description="Name of the niche opportunity")
    community: str = Field(description="Primary community or forum where this niche lives")
    spending_hypothesis: str = Field(description="Why this community spends on information products")
    information_gap_hypothesis: str = Field(description="The specific gap in available information")
    ai_leverage_theory: str = Field(description="How AI reduces creation effort for this niche")
    recommended_format: str = Field(description="Recommended product format")
    confidence: Literal["low", "medium", "high"] = Field(description="Confidence in this niche")
    validation_queries: list[str] = Field(description="Search queries to validate spending signals")


class NicheCandidateList(BaseModel):
    candidates: list[NicheCandidate] = Field(description="List of niche candidates discovered")
