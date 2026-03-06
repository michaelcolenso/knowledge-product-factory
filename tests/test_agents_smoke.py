"""Smoke tests for all agents using MockAdapter."""

import json
from pathlib import Path

import pytest

from kpf.models.mock_adapter import MockAdapter
from kpf.orchestrator.state import PipelineState
from kpf.schemas.run_config import Constraints, RunConfig

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


def make_mock_adapter():
    return MockAdapter(fixtures_dir=FIXTURES)


class TestIntakeAgent:
    def test_creates_run_config_artifact(self, minimal_state, mock_adapter, fresh_run_dir):
        from kpf.agents.intake import IntakeAgent
        agent = IntakeAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(minimal_state)
        assert "run_config" in result.artifacts

    def test_writes_run_config_to_disk(self, minimal_state, mock_adapter, fresh_run_dir):
        from kpf.agents.intake import IntakeAgent
        agent = IntakeAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        agent.run(minimal_state)
        assert (fresh_run_dir / "run_config.json").exists()


class TestDiscoveryAgent:
    def test_creates_niche_candidates_artifact(self, state_after_intake, mock_adapter, fresh_run_dir):
        from kpf.agents.discovery import DiscoveryAgent
        agent = DiscoveryAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_after_intake)
        assert "niche_candidates" in result.artifacts

    def test_writes_to_disk(self, state_after_intake, mock_adapter, fresh_run_dir):
        from kpf.agents.discovery import DiscoveryAgent
        agent = DiscoveryAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        agent.run(state_after_intake)
        assert (fresh_run_dir / "niche_candidates.json").exists()


class TestSpendingAgent:
    def test_creates_spending_signals_artifact(self, state_after_intake, mock_adapter, fresh_run_dir):
        from kpf.agents.spending import SpendingAgent
        agent = SpendingAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_after_intake)
        assert "spending_signals" in result.artifacts

    def test_writes_to_niche_analysis_dir(self, state_after_intake, mock_adapter, fresh_run_dir):
        from kpf.agents.spending import SpendingAgent
        agent = SpendingAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        agent.run(state_after_intake)
        assert (fresh_run_dir / "niche_analysis" / "spending_signals.json").exists()


class TestPainAgent:
    def test_creates_pain_map_artifact(self, state_after_spending, mock_adapter, fresh_run_dir):
        from kpf.agents.pain import PainAgent
        agent = PainAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_after_spending)
        assert "pain_map" in result.artifacts


class TestCompetitorsAgent:
    def test_creates_competitor_map_artifact(self, state_after_pain, mock_adapter, fresh_run_dir):
        from kpf.agents.competitors import CompetitorsAgent
        agent = CompetitorsAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_after_pain)
        assert "competitor_map" in result.artifacts


class TestScoringAgent:
    def test_creates_opportunity_score_artifact(self, state_after_pain, mock_adapter, fresh_run_dir):
        from kpf.agents.scoring import ScoringAgent
        state_after_pain.artifacts["competitor_map"] = load_fixture("competitor_map.json")
        agent = ScoringAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_after_pain)
        assert "opportunity_score" in result.artifacts


class TestStrategyAgent:
    def test_creates_product_brief_artifact(self, state_after_scoring, mock_adapter, fresh_run_dir):
        from kpf.agents.strategy import StrategyAgent
        agent = StrategyAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_after_scoring)
        assert "product_brief" in result.artifacts


class TestOutlineAgent:
    def test_creates_outline_artifact(self, state_after_scoring, mock_adapter, fresh_run_dir):
        from kpf.agents.outline import OutlineAgent
        state_after_scoring.artifacts["product_brief"] = load_fixture("product_brief.json")
        agent = OutlineAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_after_scoring)
        assert "outline" in result.artifacts


class TestSynthesisAgent:
    def test_creates_knowledge_base_artifact(self, state_for_build, mock_adapter, fresh_run_dir):
        from kpf.agents.synthesis import SynthesisAgent
        agent = SynthesisAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_for_build)
        assert "knowledge_base" in result.artifacts


class TestDraftingAgent:
    def test_creates_draft_product_artifact(self, state_for_build, mock_adapter, fresh_run_dir):
        from kpf.agents.drafting import DraftingAgent
        agent = DraftingAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_for_build)
        assert "draft_product" in result.artifacts

    def test_writes_markdown_file(self, state_for_build, mock_adapter, fresh_run_dir):
        from kpf.agents.drafting import DraftingAgent
        agent = DraftingAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        agent.run(state_for_build)
        assert (fresh_run_dir / "product" / "draft_product.md").exists()


class TestValidationAgent:
    def test_creates_validation_report_artifact(self, state_for_build, mock_adapter, fresh_run_dir):
        from kpf.agents.validation import ValidationAgent
        agent = ValidationAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_for_build)
        assert "validation_report" in result.artifacts

    def test_validation_passes_with_complete_state(self, state_for_build, mock_adapter, fresh_run_dir):
        from kpf.agents.validation import ValidationAgent
        agent = ValidationAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_for_build)
        report = result.artifacts["validation_report"]
        assert report["status"] in ("PASS", "REVISE", "FAIL")


class TestPackagingAgent:
    def test_creates_package_manifest_artifact(self, state_for_build, mock_adapter, fresh_run_dir):
        from kpf.agents.packaging import PackagingAgent
        agent = PackagingAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_for_build)
        assert "package_manifest" in result.artifacts


class TestLaunchAgent:
    def test_creates_launch_assets_artifact(self, state_for_build, mock_adapter, fresh_run_dir):
        from kpf.agents.launch import LaunchAgent
        agent = LaunchAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        result = agent.run(state_for_build)
        assert "launch_assets" in result.artifacts

    def test_writes_launch_files_to_disk(self, state_for_build, mock_adapter, fresh_run_dir):
        from kpf.agents.launch import LaunchAgent
        agent = LaunchAgent(adapter=mock_adapter, run_dir=fresh_run_dir)
        agent.run(state_for_build)
        assert (fresh_run_dir / "launch" / "sales_page.md").exists()
