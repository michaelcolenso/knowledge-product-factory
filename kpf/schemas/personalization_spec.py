"""PersonalizationSpec schema."""

from pydantic import BaseModel, Field


class PersonalizationSpec(BaseModel):
    input_fields: list[str] = Field(description="Fields the buyer fills in to personalize the product")
    generation_logic: list[str] = Field(description="Rules for transforming inputs into personalized outputs")
    outputs: list[str] = Field(description="What gets personalized in the final product")
    update_strategy: str = Field(description="How the product updates when inputs change")
