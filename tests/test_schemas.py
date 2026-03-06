import pytest
from pydantic import ValidationError
from kpf.schemas.run_config import RunConfig
from kpf.schemas.opportunity_score import OpportunityScore


def test_run_config_validates():
    cfg = RunConfig(mode="validate", niche="x")
    assert cfg.mode == "validate"


def test_opportunity_score_bounds_fail():
    with pytest.raises(ValidationError):
        OpportunityScore(niche="x", spending_score=11, pain_score=1, competition_score=1, total_score=13, rationale="bad")
