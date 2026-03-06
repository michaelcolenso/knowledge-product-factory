"""ArtifactManifest schema."""

from pydantic import BaseModel, Field


class ArtifactItem(BaseModel):
    name: str = Field(description="Human-readable artifact name")
    file_name: str = Field(description="Filename on disk (e.g. 'credentialing_checklist.md')")
    purpose: str = Field(description="What this artifact helps the buyer do")
    format: str = Field(description="File format: md, csv, json, txt")


class ArtifactManifest(BaseModel):
    items: list[ArtifactItem] = Field(description="All support artifacts created for this product")
