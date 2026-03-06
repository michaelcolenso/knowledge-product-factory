"""OpportunityScore schema."""

from typing import Literal

from pydantic import BaseModel, Field


class ScoreBreakdown(BaseModel):
    spending_clarity: int = Field(description="Score 1-5: how clear and quantified is the spending intent")
    information_gap: int = Field(description="Score 1-5: how specific and unmet is the information need")
    urgency: int = Field(description="Score 1-5: how time-sensitive is getting this right")
    create_feasibility: int = Field(description="Score 1-5: how feasible is creating this in 2-4 weeks")
    ai_multiplier: int = Field(description="Score 1-5: how much does AI reduce creation effort")


class OpportunityScore(BaseModel):
    scores: ScoreBreakdown = Field(description="Dimension-by-dimension score breakdown")
    total: int = Field(description="Sum of all dimension scores (max 25)")
    decision: Literal["CREATE", "PIVOT", "REJECT"] = Field(
        description="Decision: CREATE (>=18), PIVOT (13-17), REJECT (<13)"
    )
    confidence: Literal["low", "medium", "high"] = Field(description="Confidence in this assessment")
    justification: dict[str, str] = Field(description="Justification string per dimension")
