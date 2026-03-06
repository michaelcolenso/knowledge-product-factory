from pydantic import BaseModel


class KnowledgeBase(BaseModel):
    sources: list[str]
    key_insights: list[str]
