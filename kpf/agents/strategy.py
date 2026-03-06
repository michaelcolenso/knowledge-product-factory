from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.product_brief import ProductBrief
from kpf.utils.json_io import write_json


class StrategyAgent(BaseAgent):
    name = "strategy"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        brief = ProductBrief(
            niche=state.config.niche or "unknown",
            audience="private practice therapists",
            transformation="Go from rejected credentialing packets to approved panel submissions",
            product_type="playbook",
            promise="Submit clean insurer applications in 14 days",
        )
        path = state.run_dir / "product_brief.json"
        write_json(path, brief.model_dump())
        state.data["product_brief"] = brief
        state.register_artifact("product_brief", path)
        return state
