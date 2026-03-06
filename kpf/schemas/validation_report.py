from pydantic import BaseModel


class ValidationReport(BaseModel):
    gate_results: dict[str, bool]
    ready_to_ship: bool
    notes: list[str]
