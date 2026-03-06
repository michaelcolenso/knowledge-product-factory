from pydantic import BaseModel


class SpendingSignal(BaseModel):
    source: str
    signal: str
    strength: int


class SpendingSignalsReport(BaseModel):
    niche: str
    signals: list[SpendingSignal]
