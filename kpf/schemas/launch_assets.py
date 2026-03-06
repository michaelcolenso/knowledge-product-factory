from pydantic import BaseModel


class LaunchAssets(BaseModel):
    sales_page: str
    gumroad_listing: str
    faq: str
    objections: str
    launch_posts: str
