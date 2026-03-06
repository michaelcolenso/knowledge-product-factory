from pydantic import BaseModel


class ProductBrief(BaseModel):
    niche: str
    audience: str
    transformation: str
    product_type: str
    promise: str
