from pydantic import BaseModel


class PainPoint(BaseModel):
    pain: str
    specificity: str
    urgency: int


class PainMap(BaseModel):
    niche: str
    pains: list[PainPoint]
