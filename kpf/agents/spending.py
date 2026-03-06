from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.spending_signal import SpendingSignalsReport, SpendingSignal
from kpf.utils.json_io import write_json


class SpendingAgent(BaseAgent):
    name = "spending"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        niche = state.config.niche or state.require("discovery_report").niches[0].name
        report = SpendingSignalsReport(
            niche=niche,
            signals=[
                SpendingSignal(source="marketplace", signal="credentialing templates sold repeatedly", strength=4),
                SpendingSignal(source="forums", signal="therapists paying for credentialing help", strength=5),
            ],
        )
        path = state.run_dir / "spending_signals.json"
        write_json(path, report.model_dump())
        state.data["spending_signals"] = report
        state.register_artifact("spending_signals", path)
        return state
