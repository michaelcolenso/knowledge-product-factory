"""ProductBrief schema."""

from pydantic import BaseModel, Field


class ProductBrief(BaseModel):
    opportunity_name: str = Field(description="Name of this knowledge product opportunity")
    target_user: str = Field(description="Specific description of the ideal buyer")
    format: str = Field(description="Product format (playbook, SOP, template_library, etc.)")
    core_promise: str = Field(description="The main outcome the buyer gets from this product")
    price: int = Field(description="Recommended price in USD")
    ai_leverage: str = Field(description="How AI was used to make creation feasible")
    differentiator: str = Field(description="What makes this different from existing alternatives")
    deliverables: list[str] = Field(description="List of items included in the product")
    distribution_channels: list[str] = Field(description="Where and how to sell this product")
