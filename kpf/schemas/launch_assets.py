"""LaunchAssets schema."""

from pydantic import BaseModel, Field


class LaunchAssets(BaseModel):
    sales_page_md: str = Field(description="Full sales page in markdown format")
    gumroad_listing_md: str = Field(description="Gumroad product listing copy in markdown")
    lead_magnet_concept: str = Field(description="Lead magnet concept to drive list growth")
    launch_posts: list[str] = Field(description="3-5 launch posts for social media")
    faq_md: str = Field(description="Frequently asked questions in markdown format")
    objections_md: str = Field(description="Common objections and responses in markdown format")
