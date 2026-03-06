from kpf.orchestrator.state import OrchestratorState
from kpf.settings import settings


class GateFailure(RuntimeError):
    pass


def enforce_gate(name: str, state: OrchestratorState) -> None:
    ok = False
    if name == "spending":
        report = state.require("spending_signals")
        ok = len(report.signals) >= settings.min_spending_signals
    elif name == "pain":
        pain = state.require("pain_map")
        ok = len(pain.pains) >= settings.min_pain_points and all(p.specificity for p in pain.pains)
    elif name == "score":
        score = state.require("opportunity_score")
        ok = score.total_score >= state.config.min_score
    elif name == "validation":
        report = state.require("validation_report")
        ok = report.ready_to_ship
    else:
        raise ValueError(f"Unknown gate: {name}")

    state.gate_results[name] = ok
    if not ok:
        raise GateFailure(f"Gate failed: {name}")
