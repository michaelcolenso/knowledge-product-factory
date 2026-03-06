"""Schema validation tests."""

import pytest
from pydantic import ValidationError

from kpf.schemas.artifact_manifest import ArtifactItem, ArtifactManifest
from kpf.schemas.competitor_map import CompetitorItem, CompetitorMap
from kpf.schemas.knowledge_base import KnowledgeBase, KnowledgeFact
from kpf.schemas.launch_assets import LaunchAssets
from kpf.schemas.niche_candidate import NicheCandidate, NicheCandidateList
from kpf.schemas.opportunity_score import OpportunityScore, ScoreBreakdown
from kpf.schemas.outline import Outline, OutlineSection
from kpf.schemas.package_manifest import PackageManifest
from kpf.schemas.pain_map import PainMap, PainPattern
from kpf.schemas.personalization_spec import PersonalizationSpec
from kpf.schemas.product_brief import ProductBrief
from kpf.schemas.run_config import Constraints, RunConfig
from kpf.schemas.spending_signal import SpendingSignal, SpendingSignalsReport
from kpf.schemas.validation_report import ValidationReport


class TestRunConfig:
    def test_valid_construction(self):
        config = RunConfig(mode="full", niche="test niche", constraints=Constraints())
        assert config.mode == "full"
        assert config.niche == "test niche"

    def test_model_json_schema(self):
        schema = RunConfig.model_json_schema()
        assert schema is not None
        assert "properties" in schema

    def test_invalid_mode(self):
        with pytest.raises(ValidationError):
            RunConfig(mode="invalid_mode", constraints=Constraints())

    def test_defaults(self):
        config = RunConfig(mode="validate", constraints=Constraints())
        assert config.strict_mode is True
        assert config.with_personalization is False


class TestNicheCandidate:
    def test_valid_construction(self):
        candidate = NicheCandidate(
            niche_name="test niche",
            community="r/test",
            spending_hypothesis="people pay for this",
            information_gap_hypothesis="no good guide exists",
            ai_leverage_theory="AI can synthesize quickly",
            recommended_format="playbook",
            confidence="high",
            validation_queries=["query 1", "query 2"],
        )
        assert candidate.niche_name == "test niche"

    def test_invalid_confidence(self):
        with pytest.raises(ValidationError):
            NicheCandidate(
                niche_name="test",
                community="r/test",
                spending_hypothesis="x",
                information_gap_hypothesis="x",
                ai_leverage_theory="x",
                recommended_format="playbook",
                confidence="very_high",  # invalid
                validation_queries=["q1"],
            )

    def test_model_json_schema(self):
        assert NicheCandidateList.model_json_schema() is not None


class TestSpendingSignalsReport:
    def test_valid_construction(self):
        signal = SpendingSignal(
            community="r/test",
            quote="Paid $2000",
            purchase_type="consultant",
            amount_usd=2000,
            job_to_be_done="get credentialed",
            satisfaction="frustrated",
            date="2024-01",
        )
        report = SpendingSignalsReport(
            niche="test",
            signals=[signal, signal, signal],
            signal_count=3,
            passes_threshold=True,
        )
        assert report.signal_count == 3
        assert report.passes_threshold is True

    def test_optional_amount(self):
        signal = SpendingSignal(
            community="r/test",
            quote="Spent 3 hours",
            purchase_type="time",
            amount_usd=None,
            time_cost="3 hours",
            job_to_be_done="research",
            satisfaction="neutral",
            date="2024-01",
        )
        assert signal.amount_usd is None

    def test_invalid_satisfaction(self):
        with pytest.raises(ValidationError):
            SpendingSignal(
                community="r/test",
                quote="test",
                purchase_type="course",
                job_to_be_done="test",
                satisfaction="angry",  # invalid
                date="2024-01",
            )


class TestPainMap:
    def test_valid_construction(self):
        pain = PainMap(
            core_question="Which panels first?",
            patterns=[
                PainPattern(
                    type="information_gap",
                    quote="No guide exists",
                    frequency_estimate=50,
                )
            ],
            current_workarounds=["hire consultant"],
            time_wasted="3 hours",
            money_risked="$8,000",
            emotional_state="anxious",
            ideal_solution_language="step by step guide",
        )
        assert pain.core_question == "Which panels first?"

    def test_invalid_pattern_type(self):
        with pytest.raises(ValidationError):
            PainPattern(
                type="unknown_type",
                quote="test",
                frequency_estimate=10,
            )


class TestOpportunityScore:
    def test_valid_construction(self):
        score = OpportunityScore(
            scores=ScoreBreakdown(
                spending_clarity=5,
                information_gap=5,
                urgency=4,
                create_feasibility=4,
                ai_multiplier=4,
            ),
            total=22,
            decision="CREATE",
            confidence="high",
            justification={"spending_clarity": "clear evidence"},
        )
        assert score.total == 22
        assert score.decision == "CREATE"

    def test_invalid_decision(self):
        with pytest.raises(ValidationError):
            OpportunityScore(
                scores=ScoreBreakdown(
                    spending_clarity=5,
                    information_gap=5,
                    urgency=4,
                    create_feasibility=4,
                    ai_multiplier=4,
                ),
                total=22,
                decision="MAYBE",  # invalid
                confidence="high",
                justification={},
            )


class TestValidationReport:
    def test_valid_pass(self):
        report = ValidationReport(
            status="PASS",
            checks={"draft_exists": True},
            issues=[],
            required_revisions=[],
        )
        assert report.status == "PASS"

    def test_valid_fail(self):
        report = ValidationReport(
            status="FAIL",
            checks={"draft_exists": False},
            issues=["Draft is missing"],
            required_revisions=["Write the draft"],
        )
        assert report.status == "FAIL"

    def test_invalid_status(self):
        with pytest.raises(ValidationError):
            ValidationReport(
                status="INVALID",
                checks={},
                issues=[],
                required_revisions=[],
            )


class TestArtifactManifest:
    def test_valid_construction(self):
        manifest = ArtifactManifest(items=[
            ArtifactItem(
                name="Test Checklist",
                file_name="test_checklist.md",
                purpose="Help with testing",
                format="md",
            )
        ])
        assert len(manifest.items) == 1

    def test_model_json_schema(self):
        assert ArtifactManifest.model_json_schema() is not None
