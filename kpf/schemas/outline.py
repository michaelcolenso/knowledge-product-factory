"""Outline schema."""

from pydantic import BaseModel, Field


class OutlineSection(BaseModel):
    title: str = Field(description="Section title")
    goal: str = Field(description="What the reader achieves by completing this section")
    bullets: list[str] = Field(description="Key points to cover in this section")
    artifacts_referenced: list[str] = Field(
        default=[],
        description="Names of support artifacts relevant to this section",
    )


class Outline(BaseModel):
    product_title: str = Field(description="Final product title")
    sections: list[OutlineSection] = Field(description="All sections of the product in order")
