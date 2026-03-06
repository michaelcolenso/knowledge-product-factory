"""KnowledgeBase schema."""

from typing import Literal

from pydantic import BaseModel, Field


class KnowledgeFact(BaseModel):
    claim: str = Field(description="Specific, actionable knowledge claim")
    support: str = Field(description="Evidence or reasoning supporting this claim")
    confidence: Literal["low", "medium", "high"] = Field(description="Confidence level in this fact")


class KnowledgeBase(BaseModel):
    niche: str = Field(description="The niche this knowledge base covers")
    facts: list[KnowledgeFact] = Field(description="Structured facts synthesized from research")
    decisions: list[str] = Field(description="Key decisions the target user must make")
    pitfalls: list[str] = Field(description="Common mistakes to avoid")
    contradictions: list[str] = Field(description="Areas where sources or evidence conflict")
