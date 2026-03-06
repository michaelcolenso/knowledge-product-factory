"""ValidationReport schema."""

from typing import Literal

from pydantic import BaseModel, Field


class ValidationReport(BaseModel):
    status: Literal["PASS", "REVISE", "FAIL"] = Field(description="Overall validation outcome")
    checks: dict[str, bool] = Field(description="Pass/fail result per gate check")
    issues: list[str] = Field(description="Specific issues that must be addressed")
    required_revisions: list[str] = Field(description="Required changes before launch approval")
