"""Validation gates for the KPF pipeline."""

from kpf.config import MIN_ARTIFACTS, MIN_SPENDING_QUANTIFIED, MIN_SPENDING_SIGNALS, SCORE_THRESHOLD
from kpf.orchestrator.state import PipelineState
from kpf.schemas.spending_signal import SpendingSignalsReport
from kpf.schemas.pain_map import PainMap
from kpf.schemas.opportunity_score import OpportunityScore
from kpf.schemas.artifact_manifest import ArtifactManifest
from kpf.schemas.validation_report import ValidationReport
from kpf.schemas.product_brief import ProductBrief


class GateError(Exception):
    """Raised when a gate check fails."""

    def __init__(self, gate: str, reason: str) -> None:
        self.gate = gate
        self.reason = reason
        super().__init__(f"Gate '{gate}' failed: {reason}")


def enforce_spending_gate(state: PipelineState) -> None:
    """Gate 1: Spending evidence must meet minimum thresholds."""
    raw = state.artifacts.get("spending_signals")
    if raw is None:
        raise GateError("spending", "spending_signals artifact is missing from state")

    report = SpendingSignalsReport.model_validate(raw) if isinstance(raw, dict) else raw

    if report.signal_count < MIN_SPENDING_SIGNALS:
        raise GateError(
            "spending",
            f"Only {report.signal_count} spending signals found, need {MIN_SPENDING_SIGNALS}+",
        )

    quantified = sum(
        1
        for s in report.signals
        if s.amount_usd is not None or s.time_cost is not None
    )
    if quantified < MIN_SPENDING_QUANTIFIED:
        raise GateError(
            "spending",
            f"Only {quantified} quantified signals (with dollar or time cost), need {MIN_SPENDING_QUANTIFIED}+",
        )

    state.gates["spending"] = True


def enforce_pain_gate(state: PipelineState) -> None:
    """Gate 2: Pain must be specific and consequential."""
    raw = state.artifacts.get("pain_map")
    if raw is None:
        raise GateError("pain", "pain_map artifact is missing from state")

    pain = PainMap.model_validate(raw) if isinstance(raw, dict) else raw

    if not pain.core_question or len(pain.core_question.strip()) < 10:
        raise GateError("pain", "pain_map.core_question is missing or too vague")

    if not pain.current_workarounds:
        raise GateError("pain", "pain_map.current_workarounds is empty - no evidence of active pain")

    if not pain.money_risked or pain.money_risked.strip().lower() in ("", "none", "unknown"):
        raise GateError("pain", "pain_map.money_risked is not quantified")

    state.gates["pain"] = True


def enforce_score_gate(state: PipelineState) -> None:
    """Gate 3: Opportunity score must meet CREATE threshold."""
    raw = state.artifacts.get("opportunity_score")
    if raw is None:
        raise GateError("score", "opportunity_score artifact is missing from state")

    score = OpportunityScore.model_validate(raw) if isinstance(raw, dict) else raw

    if score.total < SCORE_THRESHOLD:
        raise GateError(
            "score",
            f"Opportunity score {score.total} is below threshold {SCORE_THRESHOLD}. Decision: {score.decision}",
        )

    if score.decision != "CREATE":
        raise GateError(
            "score",
            f"Decision is '{score.decision}', not 'CREATE'. Cannot proceed to build.",
        )

    state.gates["score"] = True


def enforce_artifact_gate(state: PipelineState) -> None:
    """Gate 4: Product must have draft and minimum support artifacts."""
    if "draft_product" not in state.artifacts:
        raise GateError("artifact", "draft_product is missing from state")

    raw = state.artifacts.get("artifact_manifest")
    if raw is None:
        raise GateError("artifact", "artifact_manifest is missing from state")

    manifest = ArtifactManifest.model_validate(raw) if isinstance(raw, dict) else raw

    if len(manifest.items) < MIN_ARTIFACTS:
        raise GateError(
            "artifact",
            f"Only {len(manifest.items)} support artifacts, need {MIN_ARTIFACTS}+",
        )

    if "package_manifest" not in state.artifacts:
        raise GateError("artifact", "package_manifest is missing from state")

    state.gates["artifact"] = True


def enforce_launch_gate(state: PipelineState) -> None:
    """Gate 5: Launch readiness - audience, channels, and pricing must exist."""
    raw = state.artifacts.get("validation_report")
    if raw is None:
        raise GateError("launch", "validation_report is missing from state")

    report = ValidationReport.model_validate(raw) if isinstance(raw, dict) else raw

    if report.status != "PASS":
        raise GateError(
            "launch",
            f"Validation status is '{report.status}', not 'PASS'. Issues: {'; '.join(report.issues[:3])}",
        )

    brief_raw = state.artifacts.get("product_brief")
    if brief_raw is None:
        raise GateError("launch", "product_brief is missing from state")

    brief = ProductBrief.model_validate(brief_raw) if isinstance(brief_raw, dict) else brief_raw

    if not brief.distribution_channels:
        raise GateError("launch", "product_brief.distribution_channels is empty - no launch channels defined")

    if not brief.target_user or len(brief.target_user.strip()) < 5:
        raise GateError("launch", "product_brief.target_user is not defined")

    state.gates["launch"] = True
