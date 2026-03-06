"""Shared test fixtures."""

from pathlib import Path

import pytest

from kpf.models.mock_adapter import MockAdapter
from kpf.orchestrator.state import PipelineState


@pytest.fixture
def mock_adapter():
    return MockAdapter()


@pytest.fixture
def fresh_run_dir(tmp_path):
    run_dir = tmp_path / "runs" / "test-run"
    run_dir.mkdir(parents=True)
    return run_dir


@pytest.fixture
def minimal_state(fresh_run_dir):
    return PipelineState(
        run_id="test-2026-03-06",
        mode="full",
        niche="therapist insurance credentialing",
        run_dir=fresh_run_dir,
    )


@pytest.fixture
def state_after_intake(minimal_state):
    from kpf.schemas.run_config import Constraints, RunConfig
    config = RunConfig(mode="full", niche="therapist insurance credentialing", constraints=Constraints())
    minimal_state.artifacts["run_config"] = config.model_dump()
    return minimal_state


@pytest.fixture
def state_after_spending(state_after_intake):
    import json
    fixtures = Path(__file__).parent / "fixtures"
    state_after_intake.artifacts["spending_signals"] = json.loads(
        (fixtures / "spending_signals_report.json").read_text()
    )
    state_after_intake.artifacts["niche_candidates"] = json.loads(
        (fixtures / "niche_candidate_list.json").read_text()
    )
    return state_after_intake


@pytest.fixture
def state_after_pain(state_after_spending):
    import json
    fixtures = Path(__file__).parent / "fixtures"
    state_after_spending.artifacts["pain_map"] = json.loads(
        (fixtures / "pain_map.json").read_text()
    )
    return state_after_spending


@pytest.fixture
def state_after_scoring(state_after_pain):
    import json
    fixtures = Path(__file__).parent / "fixtures"
    state_after_pain.artifacts["competitor_map"] = json.loads(
        (fixtures / "competitor_map.json").read_text()
    )
    state_after_pain.artifacts["opportunity_score"] = json.loads(
        (fixtures / "opportunity_score.json").read_text()
    )
    return state_after_pain


@pytest.fixture
def state_for_build(state_after_scoring):
    import json
    fixtures = Path(__file__).parent / "fixtures"
    state_after_scoring.artifacts["product_brief"] = json.loads(
        (fixtures / "product_brief.json").read_text()
    )
    state_after_scoring.artifacts["outline"] = json.loads(
        (fixtures / "outline.json").read_text()
    )
    state_after_scoring.artifacts["knowledge_base"] = json.loads(
        (fixtures / "knowledge_base.json").read_text()
    )
    state_after_scoring.artifacts["draft_product"] = "# Test Draft\n\nThis is the test product draft content. " * 50
    state_after_scoring.artifacts["artifact_manifest"] = json.loads(
        (fixtures / "artifact_manifest.json").read_text()
    )
    state_after_scoring.artifacts["package_manifest"] = json.loads(
        (fixtures / "package_manifest.json").read_text()
    )
    state_after_scoring.artifacts["validation_report"] = json.loads(
        (fixtures / "validation_report.json").read_text()
    )
    return state_after_scoring
