from kpf.orchestrator.engine import initialize_state
from kpf.schemas.run_config import RunConfig
from kpf.agents.intake import IntakeAgent
from kpf.agents.discovery import DiscoveryAgent
from kpf.agents.spending import SpendingAgent


def test_agents_smoke_with_mock_adapter():
    state = initialize_state(RunConfig(mode="discover"))
    state = IntakeAgent().run(state)
    state = DiscoveryAgent().run(state)
    state = SpendingAgent().run(state)
    assert "intake" in state.artifacts
    assert "discovery_report" in state.artifacts
    assert "spending_signals" in state.artifacts
