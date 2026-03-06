from pydantic import BaseModel, Field


class OpportunityScore(BaseModel):
    niche: str
    spending_score: int = Field(ge=0, le=10)
    pain_score: int = Field(ge=0, le=10)
    competition_score: int = Field(ge=0, le=10)
    total_score: int = Field(ge=0, le=30)
    rationale: str
