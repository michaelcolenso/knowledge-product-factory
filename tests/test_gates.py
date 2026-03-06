import pytest
from pathlib import Path
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.run_config import RunConfig
from kpf.schemas.spending_signal import SpendingSignalsReport, SpendingSignal
from kpf.schemas.pain_map import PainMap
from kpf.schemas.opportunity_score import OpportunityScore
from kpf.schemas.validation_report import ValidationReport
from kpf.orchestrator.gates import enforce_gate, GateFailure


def mk_state():
    return OrchestratorState(config=RunConfig(mode="validate", niche="x"), run_dir=Path("runs/test"))


def test_spending_gate_fails_low_signals():
    s = mk_state()
    s.data["spending_signals"] = SpendingSignalsReport(niche="x", signals=[SpendingSignal(source="a", signal="b", strength=1)])
    with pytest.raises(GateFailure):
        enforce_gate("spending", s)


def test_score_gate_fails_under_threshold():
    s = mk_state()
    s.data["opportunity_score"] = OpportunityScore(niche="x", spending_score=1, pain_score=1, competition_score=1, total_score=3, rationale="low")
    with pytest.raises(GateFailure):
        enforce_gate("score", s)


def test_validation_gate_missing_artifacts_fails():
    s = mk_state()
    s.data["validation_report"] = ValidationReport(gate_results={"artifacts_present": False}, ready_to_ship=False, notes=["missing"])
    with pytest.raises(GateFailure):
        enforce_gate("validation", s)
