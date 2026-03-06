"""Gate enforcement tests."""

import pytest

from kpf.orchestrator.gates import (
    GateError,
    enforce_artifact_gate,
    enforce_launch_gate,
    enforce_pain_gate,
    enforce_score_gate,
    enforce_spending_gate,
)
from kpf.orchestrator.state import PipelineState


def make_state(**artifacts) -> PipelineState:
    state = PipelineState(run_id="test", mode="full", niche="test niche")
    state.artifacts.update(artifacts)
    return state


class TestSpendingGate:
    def test_passes_with_3_quantified_signals(self):
        state = make_state(
            spending_signals={
                "niche": "test",
                "signals": [
                    {"community": "r/test", "quote": "q1", "purchase_type": "consultant", "amount_usd": 2000, "time_cost": None, "job_to_be_done": "jtbd", "satisfaction": "frustrated", "date": "2024-01"},
                    {"community": "r/test", "quote": "q2", "purchase_type": "course", "amount_usd": 500, "time_cost": None, "job_to_be_done": "jtbd2", "satisfaction": "neutral", "date": "2024-02"},
                    {"community": "r/test", "quote": "q3", "purchase_type": "time", "amount_usd": None, "time_cost": "3 hours", "job_to_be_done": "jtbd3", "satisfaction": "frustrated", "date": "2024-03"},
                ],
                "signal_count": 3,
                "passes_threshold": True,
            }
        )
        enforce_spending_gate(state)
        assert state.gates["spending"] is True

    def test_fails_with_2_signals(self):
        state = make_state(
            spending_signals={
                "niche": "test",
                "signals": [
                    {"community": "r/test", "quote": "q1", "purchase_type": "consultant", "amount_usd": 2000, "time_cost": None, "job_to_be_done": "jtbd", "satisfaction": "frustrated", "date": "2024-01"},
                    {"community": "r/test", "quote": "q2", "purchase_type": "course", "amount_usd": 500, "time_cost": None, "job_to_be_done": "jtbd2", "satisfaction": "neutral", "date": "2024-02"},
                ],
                "signal_count": 2,
                "passes_threshold": False,
            }
        )
        with pytest.raises(GateError) as exc_info:
            enforce_spending_gate(state)
        assert exc_info.value.gate == "spending"

    def test_fails_with_no_quantified_costs(self):
        state = make_state(
            spending_signals={
                "niche": "test",
                "signals": [
                    {"community": "r/test", "quote": "q1", "purchase_type": "time", "amount_usd": None, "time_cost": None, "job_to_be_done": "jtbd", "satisfaction": "frustrated", "date": "2024-01"},
                    {"community": "r/test", "quote": "q2", "purchase_type": "time", "amount_usd": None, "time_cost": None, "job_to_be_done": "jtbd2", "satisfaction": "neutral", "date": "2024-02"},
                    {"community": "r/test", "quote": "q3", "purchase_type": "time", "amount_usd": None, "time_cost": None, "job_to_be_done": "jtbd3", "satisfaction": "frustrated", "date": "2024-03"},
                ],
                "signal_count": 3,
                "passes_threshold": True,
            }
        )
        with pytest.raises(GateError) as exc_info:
            enforce_spending_gate(state)
        assert "quantified" in exc_info.value.reason.lower()

    def test_fails_missing_artifact(self):
        state = make_state()
        with pytest.raises(GateError) as exc_info:
            enforce_spending_gate(state)
        assert exc_info.value.gate == "spending"


class TestPainGate:
    def test_passes_with_valid_pain_map(self):
        state = make_state(
            pain_map={
                "core_question": "Which insurance panels should I apply to first?",
                "patterns": [{"type": "information_gap", "quote": "No guide exists", "frequency_estimate": 50}],
                "current_workarounds": ["hire consultant"],
                "time_wasted": "3 hours",
                "money_risked": "$8,000 in delayed revenue",
                "emotional_state": "anxious",
                "ideal_solution_language": "step by step guide",
            }
        )
        enforce_pain_gate(state)
        assert state.gates["pain"] is True

    def test_fails_with_vague_question(self):
        state = make_state(
            pain_map={
                "core_question": "Help",  # too vague
                "patterns": [],
                "current_workarounds": ["consultant"],
                "time_wasted": "hours",
                "money_risked": "$8000",
                "emotional_state": "stressed",
                "ideal_solution_language": "guide",
            }
        )
        with pytest.raises(GateError) as exc_info:
            enforce_pain_gate(state)
        assert exc_info.value.gate == "pain"

    def test_fails_no_workarounds(self):
        state = make_state(
            pain_map={
                "core_question": "Which insurance panels to join first?",
                "patterns": [],
                "current_workarounds": [],  # empty
                "time_wasted": "3 hours",
                "money_risked": "$8,000",
                "emotional_state": "anxious",
                "ideal_solution_language": "guide",
            }
        )
        with pytest.raises(GateError) as exc_info:
            enforce_pain_gate(state)
        assert "workaround" in exc_info.value.reason.lower()


class TestScoreGate:
    def test_passes_at_18(self):
        state = make_state(
            opportunity_score={
                "scores": {"spending_clarity": 4, "information_gap": 4, "urgency": 3, "create_feasibility": 4, "ai_multiplier": 3},
                "total": 18,
                "decision": "CREATE",
                "confidence": "medium",
                "justification": {},
            }
        )
        enforce_score_gate(state)
        assert state.gates["score"] is True

    def test_fails_at_17(self):
        state = make_state(
            opportunity_score={
                "scores": {"spending_clarity": 3, "information_gap": 4, "urgency": 3, "create_feasibility": 4, "ai_multiplier": 3},
                "total": 17,
                "decision": "PIVOT",
                "confidence": "medium",
                "justification": {},
            }
        )
        with pytest.raises(GateError) as exc_info:
            enforce_score_gate(state)
        assert exc_info.value.gate == "score"

    def test_fails_on_pivot_decision(self):
        state = make_state(
            opportunity_score={
                "scores": {"spending_clarity": 4, "information_gap": 4, "urgency": 3, "create_feasibility": 4, "ai_multiplier": 3},
                "total": 18,
                "decision": "PIVOT",  # decision doesn't match score
                "confidence": "medium",
                "justification": {},
            }
        )
        with pytest.raises(GateError) as exc_info:
            enforce_score_gate(state)
        assert "PIVOT" in exc_info.value.reason


class TestArtifactGate:
    def test_passes_with_3_artifacts(self):
        state = make_state(
            draft_product="# Test\n" * 100,
            artifact_manifest={
                "items": [
                    {"name": "A1", "file_name": "a1.md", "purpose": "p1", "format": "md"},
                    {"name": "A2", "file_name": "a2.csv", "purpose": "p2", "format": "csv"},
                    {"name": "A3", "file_name": "a3.md", "purpose": "p3", "format": "md"},
                ]
            },
            package_manifest={"product_name": "Test", "version": "1.0", "tier": "Core", "included_files": ["a.md"], "delivery_notes": ["read it"]},
        )
        enforce_artifact_gate(state)
        assert state.gates["artifact"] is True

    def test_fails_with_2_artifacts(self):
        state = make_state(
            draft_product="# Test\n" * 100,
            artifact_manifest={
                "items": [
                    {"name": "A1", "file_name": "a1.md", "purpose": "p1", "format": "md"},
                    {"name": "A2", "file_name": "a2.csv", "purpose": "p2", "format": "csv"},
                ]
            },
            package_manifest={"product_name": "Test", "version": "1.0", "tier": "Core", "included_files": ["a.md"], "delivery_notes": ["read it"]},
        )
        with pytest.raises(GateError) as exc_info:
            enforce_artifact_gate(state)
        assert exc_info.value.gate == "artifact"

    def test_fails_missing_draft(self):
        state = make_state(
            artifact_manifest={"items": []},
        )
        with pytest.raises(GateError) as exc_info:
            enforce_artifact_gate(state)
        assert "draft" in exc_info.value.reason.lower()


class TestLaunchGate:
    def test_passes_with_valid_validation(self):
        state = make_state(
            validation_report={
                "status": "PASS",
                "checks": {},
                "issues": [],
                "required_revisions": [],
            },
            product_brief={
                "opportunity_name": "Test",
                "target_user": "Test user description",
                "format": "playbook",
                "core_promise": "Get X done",
                "price": 97,
                "ai_leverage": "AI helped",
                "differentiator": "unique",
                "deliverables": ["guide"],
                "distribution_channels": ["r/test"],
            },
        )
        enforce_launch_gate(state)
        assert state.gates["launch"] is True

    def test_fails_on_revise_status(self):
        state = make_state(
            validation_report={
                "status": "REVISE",
                "checks": {},
                "issues": ["Draft is thin"],
                "required_revisions": ["Expand section 2"],
            },
            product_brief={
                "opportunity_name": "Test",
                "target_user": "Test user",
                "format": "playbook",
                "core_promise": "Get X",
                "price": 97,
                "ai_leverage": "AI",
                "differentiator": "unique",
                "deliverables": ["guide"],
                "distribution_channels": ["r/test"],
            },
        )
        with pytest.raises(GateError) as exc_info:
            enforce_launch_gate(state)
        assert exc_info.value.gate == "launch"
