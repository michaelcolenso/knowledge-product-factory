"""Run record storage using SQLModel."""

import json
from typing import Optional

from sqlmodel import Field, Session, SQLModel, select

from kpf.orchestrator.state import PipelineState
from kpf.storage.db import create_tables, get_engine
from kpf.utils.dates import today_str


class RunRecord(SQLModel, table=True):
    __tablename__ = "runs"

    id: str = Field(primary_key=True)
    mode: str
    niche: Optional[str] = None
    created_at: str
    status: str  # "running" | "complete" | "failed" | "gated"
    artifact_paths: str = "{}"  # JSON dict


class RunStore:
    def __init__(self) -> None:
        create_tables()

    def create(self, state: PipelineState) -> RunRecord:
        record = RunRecord(
            id=state.run_id,
            mode=state.mode,
            niche=state.niche,
            created_at=today_str(),
            status="running",
            artifact_paths=json.dumps({}),
        )
        with Session(get_engine()) as session:
            session.add(record)
            session.commit()
            session.refresh(record)
        return record

    def update_status(self, run_id: str, status: str) -> None:
        with Session(get_engine()) as session:
            record = session.get(RunRecord, run_id)
            if record:
                record.status = status
                session.add(record)
                session.commit()

    def get(self, run_id: str) -> Optional[RunRecord]:
        with Session(get_engine()) as session:
            return session.get(RunRecord, run_id)

    def list_all(self) -> list[RunRecord]:
        with Session(get_engine()) as session:
            return list(session.exec(select(RunRecord)).all())
