from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.knowledge_base import KnowledgeBase
from kpf.utils.json_io import write_json


class SynthesisAgent(BaseAgent):
    name = "synthesis"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        kb = KnowledgeBase(
            sources=["payer docs", "therapist forums", "credentialing SOPs"],
            key_insights=["packet completeness beats speed", "follow-up scripts reduce limbo", "taxonomy errors cause denials"],
        )
        path = state.run_dir / "knowledge_base.json"
        write_json(path, kb.model_dump())
        state.data["knowledge_base"] = kb
        state.register_artifact("knowledge_base", path)
        return state
