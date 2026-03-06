from pydantic import BaseModel


class OutlineSection(BaseModel):
    title: str
    bullets: list[str]


class Outline(BaseModel):
    title: str
    sections: list[OutlineSection]
