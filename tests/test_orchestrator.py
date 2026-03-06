"""Orchestrator pipeline tests."""

from pathlib import Path

import pytest

from kpf.models.mock_adapter import MockAdapter
from kpf.orchestrator.engine import PipelineEngine
from kpf.orchestrator.gates import GateError
from kpf.orchestrator.state import PipelineState
from kpf.schemas.run_config import Constraints, RunConfig


def make_engine_and_adapter(fixtures_dir: Path):
    adapter = MockAdapter(fixtures_dir=fixtures_dir)
    engine = PipelineEngine()
    return engine, adapter


FIXTURES = Path(__file__).parent / "fixtures"


class TestDiscoverMode:
    def test_discover_mode_stops_after_discovery(self, tmp_path):
        engine, adapter = make_engine_and_adapter(FIXTURES)
        config = RunConfig(mode="discover", constraints=Constraints())

        # Mock the runs dir to use tmp_path
        import kpf.paths as paths_module
        original = paths_module.RUNS_DIR
        paths_module.RUNS_DIR = tmp_path / "runs"
        try:
            state = engine.run(config, adapter)
        finally:
            paths_module.RUNS_DIR = original

        assert state.mode == "discover"
        assert "niche_candidates" in state.artifacts
        assert "spending_signals" not in state.artifacts


class TestValidateMode:
    def test_validate_mode_stops_after_scoring(self, tmp_path):
        engine, adapter = make_engine_and_adapter(FIXTURES)
        config = RunConfig(
            mode="validate",
            niche="therapist insurance credentialing",
            constraints=Constraints(),
        )

        import kpf.paths as paths_module
        original = paths_module.RUNS_DIR
        paths_module.RUNS_DIR = tmp_path / "runs"
        try:
            state = engine.run(config, adapter)
        finally:
            paths_module.RUNS_DIR = original

        assert "opportunity_score" in state.artifacts
        assert "product_brief" not in state.artifacts


class TestRouter:
    def test_router_discover_mode(self):
        from kpf.orchestrator.router import (
            should_run_discovery,
            should_run_validation,
            should_run_build,
            stop_after_discovery,
        )
        config = RunConfig(mode="discover", constraints=Constraints())
        assert should_run_discovery(config) is True
        assert should_run_validation(config) is False
        assert should_run_build(config) is False
        assert stop_after_discovery(config) is True

    def test_router_validate_mode(self):
        from kpf.orchestrator.router import (
            should_run_discovery,
            should_run_validation,
            stop_after_validation,
        )
        config = RunConfig(mode="validate", niche="test", constraints=Constraints())
        assert should_run_discovery(config) is False
        assert should_run_validation(config) is True
        assert stop_after_validation(config) is True

    def test_router_full_mode(self):
        from kpf.orchestrator.router import (
            should_run_build,
            should_run_launch,
            should_run_validation,
        )
        config = RunConfig(mode="full", niche="test", constraints=Constraints())
        assert should_run_validation(config) is True
        assert should_run_build(config) is True
        assert should_run_launch(config) is True
