"""PainMap schema."""

from typing import Literal

from pydantic import BaseModel, Field


class PainPattern(BaseModel):
    type: Literal["information_gap", "frustration", "competitor_failure", "time_loss", "money_risk"] = Field(
        description="Category of pain pattern"
    )
    quote: str = Field(description="Evidence quote demonstrating this pain")
    frequency_estimate: int = Field(description="Estimated frequency of this pattern (occurrences per month)")


class PainMap(BaseModel):
    core_question: str = Field(description="The single most common unanswered question in this niche")
    patterns: list[PainPattern] = Field(description="Recurring pain patterns identified")
    current_workarounds: list[str] = Field(description="How people currently deal with the pain")
    time_wasted: str = Field(description="Quantified time cost of the problem")
    money_risked: str = Field(description="Quantified financial risk of getting it wrong")
    emotional_state: str = Field(description="Emotional state of people experiencing this pain")
    ideal_solution_language: str = Field(description="Language users use when describing their ideal solution")
