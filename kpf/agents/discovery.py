"""DiscoveryAgent - generates niche candidates when no niche is provided."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.niche_candidate import NicheCandidateList


class DiscoveryAgent(BaseAgent):
    name = "discovery"
    requires: list[str] = ["run_config"]

    def _execute(self, state: PipelineState) -> PipelineState:
        run_config = state.artifacts["run_config"]
        context = f"Mode: {state.mode}\nConfig: {run_config}"

        raw = self.generate_structured(context, NicheCandidateList)
        candidates = self.parse_with_repair(raw, NicheCandidateList)

        self.write_artifact("niche_candidates.json", candidates)
        state.artifacts["niche_candidates"] = self.artifact_dict(candidates)
        state.log(f"DiscoveryAgent: {len(candidates.candidates)} candidates found")
        return state
