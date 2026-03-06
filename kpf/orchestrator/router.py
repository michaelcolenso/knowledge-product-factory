from kpf.agents.intake import IntakeAgent
from kpf.agents.discovery import DiscoveryAgent
from kpf.agents.spending import SpendingAgent
from kpf.agents.pain import PainAgent
from kpf.agents.competitors import CompetitorsAgent
from kpf.agents.scoring import ScoringAgent
from kpf.agents.strategy import StrategyAgent
from kpf.agents.outline import OutlineAgent
from kpf.agents.synthesis import SynthesisAgent
from kpf.agents.drafting import DraftingAgent
from kpf.agents.artifacts import ArtifactsAgent
from kpf.agents.personalization import PersonalizationAgent
from kpf.agents.packaging import PackagingAgent
from kpf.agents.validation import ValidationAgent
from kpf.agents.launch import LaunchAgent
from kpf.agents.retrospective import RetrospectiveAgent


def get_agent(agent_name: str):
    return {
        "intake": IntakeAgent,
        "discovery": DiscoveryAgent,
        "spending": SpendingAgent,
        "pain": PainAgent,
        "competitors": CompetitorsAgent,
        "scoring": ScoringAgent,
        "strategy": StrategyAgent,
        "outline": OutlineAgent,
        "synthesis": SynthesisAgent,
        "drafting": DraftingAgent,
        "artifacts": ArtifactsAgent,
        "personalization": PersonalizationAgent,
        "packaging": PackagingAgent,
        "validation": ValidationAgent,
        "launch": LaunchAgent,
        "retrospective": RetrospectiveAgent,
    }[agent_name]
