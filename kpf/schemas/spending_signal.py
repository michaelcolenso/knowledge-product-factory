"""SpendingSignal schemas."""

from typing import Literal

from pydantic import BaseModel, Field


class SpendingSignal(BaseModel):
    community: str = Field(description="Community or platform where signal was found")
    quote: str = Field(description="Verbatim or paraphrased evidence of spending intent")
    purchase_type: str = Field(description="Type of purchase: course, consultant, tool, etc.")
    amount_usd: int | None = Field(default=None, description="Dollar amount if quantified")
    time_cost: str | None = Field(default=None, description="Time cost if quantified (e.g. '3 hours/week')")
    job_to_be_done: str = Field(description="What the buyer is trying to accomplish")
    satisfaction: Literal["happy", "neutral", "frustrated"] = Field(
        description="Buyer satisfaction with current solutions"
    )
    date: str = Field(description="Approximate date of signal (YYYY-MM or YYYY)")


class SpendingSignalsReport(BaseModel):
    niche: str = Field(description="The niche being analyzed")
    signals: list[SpendingSignal] = Field(description="List of spending signals found")
    signal_count: int = Field(description="Total number of signals")
    passes_threshold: bool = Field(description="Whether the threshold of 3+ signals is met")
