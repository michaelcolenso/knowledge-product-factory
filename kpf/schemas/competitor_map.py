"""CompetitorMap schema."""

from typing import Literal

from pydantic import BaseModel, Field


class CompetitorItem(BaseModel):
    name: str = Field(description="Name of the competitor or alternative solution")
    category: Literal["free", "course", "consultant", "software", "community"] = Field(
        description="Category of the alternative"
    )
    price: str = Field(description="Price or price range (e.g. 'Free', '$500/month', '$2000 one-time')")
    weaknesses: list[str] = Field(description="Specific reasons this alternative fails users")


class CompetitorMap(BaseModel):
    niche: str = Field(description="The niche being analyzed")
    alternatives: list[CompetitorItem] = Field(description="Existing alternatives in the market")
    market_gap_summary: str = Field(description="Summary of the gap that existing solutions don't fill")
    switching_reason: str = Field(description="Primary reason buyers would switch to a new solution")
