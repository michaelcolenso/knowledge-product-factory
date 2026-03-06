from pydantic import BaseModel, Field


class NicheCandidate(BaseModel):
    name: str
    audience: str
    problem_summary: str
    format_fit: str
    feasible_in_weeks: int = Field(ge=1, le=8)


class DiscoveryReport(BaseModel):
    niches: list[NicheCandidate]
