"""PackageManifest schema."""

from pydantic import BaseModel, Field


class PackageManifest(BaseModel):
    product_name: str = Field(description="Buyer-facing product name")
    version: str = Field(description="Product version (e.g. '1.0')")
    tier: str = Field(description="Product tier or edition name")
    included_files: list[str] = Field(description="All files included in the product package")
    delivery_notes: list[str] = Field(description="Instructions for buyers on using the product")
