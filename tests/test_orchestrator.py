from pathlib import Path
from kpf.orchestrator.engine import run_pipeline
from kpf.schemas.run_config import RunConfig


def test_discover_mode_stops_after_discovery():
    state = run_pipeline(RunConfig(mode="discover"))
    assert "discovery_report" in state.data
    assert "spending_signals" not in state.data


def test_validate_mode_stops_after_scoring():
    state = run_pipeline(RunConfig(mode="validate", niche="therapist insurance credentialing"))
    assert "opportunity_score" in state.data
    assert "product_brief" not in state.data


def test_full_mode_writes_expected_files():
    state = run_pipeline(RunConfig(mode="full", niche="therapist insurance credentialing", with_personalization=True))
    expected = [
        "spending_signals.json",
        "pain_map.json",
        "competitor_map.json",
        "opportunity_score.json",
        "product_brief.json",
        "outline.json",
        "knowledge_base.json",
        "draft_product.md",
        "artifact_manifest.json",
        "personalization_spec.json",
        "package_manifest.json",
        "validation_report.json",
    ]
    for e in expected:
        assert (state.run_dir / e).exists(), e
    assert (state.run_dir / "launch" / "sales_page.md").exists()


def test_launch_mode_includes_discovery_phase():
    state = run_pipeline(RunConfig(mode="launch", niche="therapist insurance credentialing"))
    assert "discovery_report" in state.data
    assert "product_brief" in state.data
    assert "validation_report" in state.data
    assert (state.run_dir / "launch" / "sales_page.md").exists()


def test_build_mode_includes_discovery_and_stops_before_launch():
    state = run_pipeline(RunConfig(mode="build", niche="therapist insurance credentialing"))
    assert "discovery_report" in state.data
    assert "package_manifest" in state.data
    assert "validation_report" not in state.data
    assert not (state.run_dir / "launch" / "sales_page.md").exists()
