from pydantic import BaseModel


class Competitor(BaseModel):
    name: str
    offer: str
    price: str
    gap: str


class CompetitorMap(BaseModel):
    niche: str
    competitors: list[Competitor]
