# knowledge-product-factory

Implementation Spec — Knowledge Product Factory (KPF)

Purpose: Give another assistant enough structure to build the system without guessing.

⸻

1. Build Objective

Create a CLI-driven, schema-first, multi-agent system that:
	1.	discovers promising knowledge-product niches
	2.	validates them using spending and pain evidence
	3.	generates product briefs and artifacts
	4.	packages sale-ready outputs
	5.	blocks weak products from shipping

This is a knowledge product factory, not a general agent framework.

⸻

2. Core Product Constraints

The system should optimize for:
	•	downloadable info products, not SaaS
	•	2–4 week creator-feasible products
	•	strong evidence before generation
	•	reusable structured outputs
	•	human review at validation gates

Supported formats in v1:
	•	playbook
	•	SOP
	•	template library
	•	decision framework
	•	checklist pack
	•	Notion system
	•	research brief

Not supported in v1:
	•	full software products
	•	enterprise consulting deliverables
	•	giant video courses
	•	membership communities
	•	ad-dependent businesses

⸻

3. Technical Requirements

Language

Python 3.12+

Suggested Libraries
	•	typer for CLI
	•	pydantic for schemas
	•	jinja2 for templating
	•	sqlite3 or sqlmodel for persistence
	•	pathlib for file handling
	•	orjson or json for structured artifacts
	•	rich for terminal output
	•	markdown or plain .md outputs for drafts

Model Abstraction

Implement provider adapters so the system can swap models.

Required adapter interface:

class ModelAdapter(Protocol):
    def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str: ...

Support these adapter placeholders:
	•	OpenAIAdapter
	•	AnthropicAdapter
	•	GeminiAdapter
	•	MockAdapter

⸻

4. File Tree

kpf/
├── README.md
├── pyproject.toml
├── .env.example
├── kpf/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── settings.py
│   ├── logger.py
│   ├── paths.py
│   ├── models/
│   │   ├── adapter_base.py
│   │   ├── openai_adapter.py
│   │   ├── anthropic_adapter.py
│   │   ├── gemini_adapter.py
│   │   └── mock_adapter.py
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── run.py
│   │   ├── review.py
│   │   ├── export.py
│   │   └── inspect.py
│   ├── orchestrator/
│   │   ├── engine.py
│   │   ├── router.py
│   │   ├── state.py
│   │   └── gates.py
│   ├── agents/
│   │   ├── base.py
│   │   ├── intake.py
│   │   ├── discovery.py
│   │   ├── spending.py
│   │   ├── pain.py
│   │   ├── competitors.py
│   │   ├── scoring.py
│   │   ├── strategy.py
│   │   ├── outline.py
│   │   ├── synthesis.py
│   │   ├── drafting.py
│   │   ├── artifacts.py
│   │   ├── personalization.py
│   │   ├── packaging.py
│   │   ├── launch.py
│   │   ├── validation.py
│   │   └── retrospective.py
│   ├── prompts/
│   │   ├── intake/
│   │   │   ├── system.md
│   │   │   ├── task.md
│   │   │   └── validator.md
│   │   ├── discovery/
│   │   ├── spending/
│   │   ├── pain/
│   │   ├── competitors/
│   │   ├── scoring/
│   │   ├── strategy/
│   │   ├── outline/
│   │   ├── synthesis/
│   │   ├── drafting/
│   │   ├── artifacts/
│   │   ├── personalization/
│   │   ├── packaging/
│   │   ├── launch/
│   │   ├── validation/
│   │   └── retrospective/
│   ├── schemas/
│   │   ├── run_config.py
│   │   ├── niche_candidate.py
│   │   ├── spending_signal.py
│   │   ├── pain_map.py
│   │   ├── competitor_map.py
│   │   ├── opportunity_score.py
│   │   ├── product_brief.py
│   │   ├── outline.py
│   │   ├── knowledge_base.py
│   │   ├── artifact_manifest.py
│   │   ├── personalization_spec.py
│   │   ├── package_manifest.py
│   │   ├── launch_assets.py
│   │   └── validation_report.py
│   ├── storage/
│   │   ├── db.py
│   │   ├── run_store.py
│   │   ├── artifact_store.py
│   │   └── memory_store.py
│   ├── templates/
│   │   ├── sales_page.md.j2
│   │   ├── gumroad_listing.md.j2
│   │   ├── lead_magnet.md.j2
│   │   └── package_manifest.json.j2
│   ├── utils/
│   │   ├── files.py
│   │   ├── json_io.py
│   │   ├── markdown.py
│   │   ├── text.py
│   │   ├── slug.py
│   │   └── dates.py
│   └── memory/
│       ├── winning_niches.json
│       ├── failed_niches.json
│       ├── search_patterns.json
│       └── format_performance.json
├── runs/
├── briefs/
├── products/
└── tests/
    ├── test_schemas.py
    ├── test_gates.py
    ├── test_orchestrator.py
    └── test_agents_smoke.py


⸻

5. CLI Commands

Required Commands

kpf run discover
kpf run validate --niche "therapist insurance credentialing"
kpf run build --brief briefs/insurance_panel_accelerator.json
kpf run launch --product runs/2026-03-05_x/product/
kpf run full --niche "therapist insurance credentialing"
kpf review runs/2026-03-05_x/
kpf inspect runs/2026-03-05_x/
kpf export runs/2026-03-05_x/ --format pdf

Required Flags

--max-weeks 3
--price-floor 79
--price-ceiling 199
--formats playbook,template_library,notion_system
--with-personalization
--strict
--output-dir ./runs/custom_slug/
--model openai
--temperature 0.2


⸻

6. Orchestrator Behavior

The orchestrator must run agents in sequence and enforce gates.

Flow

intake
→ discovery (if no niche)
→ spending
→ pain
→ competitors
→ scoring
→ strategy
→ outline
→ synthesis
→ drafting
→ artifacts
→ personalization (optional)
→ packaging
→ validation
→ launch
→ retrospective

Routing Rules
	•	If mode is discover, stop after discovery.
	•	If mode is validate, stop after scoring.
	•	If opportunity score < 18, do not proceed to build.
	•	If validation status != PASS, do not proceed to launch.
	•	If --with-personalization is false, skip personalization agent.
	•	If product format does not benefit from personalization, skip regardless of flag.

⸻

7. Base Agent Contract

Every agent must implement the same interface.

from abc import ABC, abstractmethod
from typing import Any

class BaseAgent(ABC):
    name: str

    @abstractmethod
    def run(self, state: dict[str, Any]) -> dict[str, Any]:
        """Read from state, produce structured output, and return updated state."""

Each agent must:
	•	read required upstream artifacts
	•	write exactly one primary artifact
	•	log what it consumed
	•	fail loudly if prerequisites are missing

⸻

8. State Object

The orchestrator passes a shared state dict across agents.

Minimum state shape

state = {
    "run_id": "2026-03-05_therapist-insurance-credentialing",
    "mode": "full",
    "niche": "therapist insurance credentialing",
    "artifacts": {},
    "config": {},
    "logs": [],
    "gates": {},
}

Artifacts should be attached by canonical key:

state["artifacts"]["run_config"]
state["artifacts"]["niche_candidates"]
state["artifacts"]["spending_signals"]
state["artifacts"]["pain_map"]
state["artifacts"]["competitor_map"]
state["artifacts"]["opportunity_score"]
state["artifacts"]["product_brief"]
state["artifacts"]["outline"]
state["artifacts"]["knowledge_base"]
state["artifacts"]["draft_product"]
state["artifacts"]["artifact_manifest"]
state["artifacts"]["personalization_spec"]
state["artifacts"]["package_manifest"]
state["artifacts"]["launch_assets"]
state["artifacts"]["validation_report"]
state["artifacts"]["postmortem"]


⸻

9. Pydantic Schemas

RunConfig

from pydantic import BaseModel, Field
from typing import Literal

class Constraints(BaseModel):
    max_creation_weeks: int = 3
    allowed_formats: list[str] = ["playbook", "template_library", "notion_system"]
    price_floor: int = 79
    price_ceiling: int = 199

class RunConfig(BaseModel):
    mode: Literal["discover", "validate", "build", "launch", "full"]
    niche: str | None = None
    target_audience: str | None = None
    constraints: Constraints
    strict_mode: bool = True
    with_personalization: bool = False

NicheCandidate

class NicheCandidate(BaseModel):
    niche_name: str
    community: str
    spending_hypothesis: str
    information_gap_hypothesis: str
    ai_leverage_theory: str
    recommended_format: str
    confidence: Literal["low", "medium", "high"]
    validation_queries: list[str]

SpendingSignal

class SpendingSignal(BaseModel):
    community: str
    quote: str
    purchase_type: str
    amount_usd: int | None = None
    time_cost: str | None = None
    job_to_be_done: str
    satisfaction: Literal["happy", "neutral", "frustrated"]
    date: str

SpendingSignalsReport

class SpendingSignalsReport(BaseModel):
    niche: str
    signals: list[SpendingSignal]
    signal_count: int
    passes_threshold: bool

PainPattern

class PainPattern(BaseModel):
    type: Literal["information_gap", "frustration", "competitor_failure", "time_loss", "money_risk"]
    quote: str
    frequency_estimate: int

PainMap

class PainMap(BaseModel):
    core_question: str
    patterns: list[PainPattern]
    current_workarounds: list[str]
    time_wasted: str
    money_risked: str
    emotional_state: str
    ideal_solution_language: str

CompetitorItem

class CompetitorItem(BaseModel):
    name: str
    category: Literal["free", "course", "consultant", "software", "community"]
    price: str
    weaknesses: list[str]

CompetitorMap

class CompetitorMap(BaseModel):
    niche: str
    alternatives: list[CompetitorItem]
    market_gap_summary: str
    switching_reason: str

OpportunityScore

class ScoreBreakdown(BaseModel):
    spending_clarity: int
    information_gap: int
    urgency: int
    create_feasibility: int
    ai_multiplier: int

class OpportunityScore(BaseModel):
    scores: ScoreBreakdown
    total: int
    decision: Literal["CREATE", "PIVOT", "REJECT"]
    confidence: Literal["low", "medium", "high"]
    justification: dict[str, str]

ProductBrief

class ProductBrief(BaseModel):
    opportunity_name: str
    target_user: str
    format: str
    core_promise: str
    price: int
    ai_leverage: str
    differentiator: str
    deliverables: list[str]
    distribution_channels: list[str]

OutlineSection

class OutlineSection(BaseModel):
    title: str
    goal: str
    bullets: list[str]
    artifacts_referenced: list[str] = []

Outline

class Outline(BaseModel):
    product_title: str
    sections: list[OutlineSection]

KnowledgeBase

class KnowledgeFact(BaseModel):
    claim: str
    support: str
    confidence: Literal["low", "medium", "high"]

class KnowledgeBase(BaseModel):
    niche: str
    facts: list[KnowledgeFact]
    decisions: list[str]
    pitfalls: list[str]
    contradictions: list[str]

ArtifactManifest

class ArtifactItem(BaseModel):
    name: str
    file_name: str
    purpose: str
    format: str

class ArtifactManifest(BaseModel):
    items: list[ArtifactItem]

PersonalizationSpec

class PersonalizationSpec(BaseModel):
    input_fields: list[str]
    generation_logic: list[str]
    outputs: list[str]
    update_strategy: str

PackageManifest

class PackageManifest(BaseModel):
    product_name: str
    version: str
    tier: str
    included_files: list[str]
    delivery_notes: list[str]

ValidationReport

class ValidationReport(BaseModel):
    status: Literal["PASS", "REVISE", "FAIL"]
    checks: dict[str, bool]
    issues: list[str]
    required_revisions: list[str]


⸻

10. Agent Responsibilities

IntakeAgent

Build run_config.

Must:
	•	normalize user input
	•	infer mode
	•	set constraints
	•	create run directory

DiscoveryAgent

Build niche_candidates.

Must:
	•	generate 5–10 niches
	•	include community, spend hypothesis, AI leverage, format, validation path

SpendingAgent

Build spending_signals.

Must:
	•	capture 3+ concrete signals
	•	reject vague chatter
	•	include dollar or time cost where possible

PainAgent

Build pain_map.

Must:
	•	identify recurring unanswered question
	•	quantify consequences
	•	capture user language

CompetitorsAgent

Build competitor_map.

Must:
	•	list alternatives
	•	map price anchors
	•	explain why current options fail

ScoringAgent

Build opportunity_score.

Must:
	•	use 1–5 integer scoring only
	•	justify every dimension
	•	decide CREATE/PIVOT/REJECT

StrategyAgent

Build product_brief.

Must:
	•	define offer
	•	define format
	•	define pricing
	•	define differentiator
	•	define channel strategy

OutlineAgent

Build outline.

Must:
	•	create section-level structure
	•	map key artifact references
	•	keep scope buildable in 2–4 weeks

SynthesisAgent

Build knowledge_base.

Must:
	•	transform source material into structured facts
	•	note contradictions
	•	mark confidence

DraftingAgent

Build draft_product.md.

Must:
	•	produce useful density
	•	avoid filler
	•	include examples and implementation steps

ArtifactsAgent

Build artifact_manifest and actual artifact files.

Must:
	•	create at least 3 support artifacts unless format clearly does not need them

PersonalizationAgent

Build personalization_spec.

Must:
	•	define inputs
	•	define transformation logic
	•	define outputs
	•	skip if not justified

PackagingAgent

Build package_manifest.

Must:
	•	define buyer-facing product stack
	•	define included files
	•	define version

LaunchAgent

Build launch assets.

Must create:
	•	sales page
	•	listing copy
	•	lead magnet concept
	•	3–5 launch posts
	•	FAQ
	•	objection handling

ValidationAgent

Build validation_report.

Must:
	•	enforce all gates
	•	veto weak or incomplete products

RetrospectiveAgent

Build postmortem.

Must:
	•	record failures and wins
	•	update memory files

⸻

11. Validation Gates

Gate 1 — Spending Evidence

Pass only if:
	•	signal_count >= 3
	•	at least 2 quantified dollar or time costs
	•	clear job-to-be-done exists

Gate 2 — Pain Specificity

Pass only if:
	•	a specific question is documented
	•	current workaround exists
	•	getting it wrong has cost

Gate 3 — Score Threshold

Pass only if:
	•	total >= 18
	•	decision = CREATE

Gate 4 — Artifact Completeness

Pass only if:
	•	main draft exists
	•	at least 3 support artifacts exist
	•	package manifest exists

Gate 5 — Launch Readiness

Pass only if:
	•	clear audience exists
	•	first 100 buyer channels exist
	•	pricing and positioning are explicit

⸻

12. Prompt Loading Rules

Each agent must load 3 prompt files:
	•	system.md
	•	task.md
	•	validator.md

The assistant building this should not hardcode giant prompts in Python.

Use filesystem-based prompt loading:

def load_prompt(agent_name: str, prompt_type: str) -> str:
    path = Path("kpf/prompts") / agent_name / f"{prompt_type}.md"
    return path.read_text()


⸻

13. Artifact Writing Rules

Every primary artifact must be saved both:
	•	in memory state
	•	on disk in the current run directory

Example output path:

runs/2026-03-05_therapist-insurance-credentialing/
├── run_config.json
├── niche_analysis/
│   ├── spending_signals.json
│   ├── pain_map.json
│   ├── competitor_map.json
│   └── opportunity_score.json
├── product/
│   ├── product_brief.json
│   ├── outline.json
│   ├── knowledge_base.json
│   ├── draft_product.md
│   ├── artifacts/
│   │   ├── credentialing_checklist.md
│   │   ├── revenue_calculator.csv
│   │   └── followup_email_scripts.md
│   └── personalization_spec.json
├── package/
│   └── package_manifest.json
├── launch/
│   ├── sales_page.md
│   ├── gumroad_listing.md
│   ├── faq.md
│   ├── objections.md
│   └── launch_posts.md
└── validation_report.json


⸻

14. Orchestrator Pseudocode

def run_pipeline(config: RunConfig) -> dict:
    state = initialize_state(config)

    state = IntakeAgent().run(state)

    if not config.niche and config.mode in {"discover", "full"}:
        state = DiscoveryAgent().run(state)
        if config.mode == "discover":
            return state

    if config.mode in {"validate", "full"}:
        state = SpendingAgent().run(state)
        enforce_gate("spending", state)

        state = PainAgent().run(state)
        enforce_gate("pain", state)

        state = CompetitorsAgent().run(state)
        state = ScoringAgent().run(state)
        enforce_gate("score", state)

        if config.mode == "validate":
            return state

    if config.mode in {"build", "full"}:
        state = StrategyAgent().run(state)
        state = OutlineAgent().run(state)
        state = SynthesisAgent().run(state)
        state = DraftingAgent().run(state)
        state = ArtifactsAgent().run(state)

        if config.with_personalization:
            state = PersonalizationAgent().run(state)

        state = PackagingAgent().run(state)
        state = ValidationAgent().run(state)
        enforce_gate("validation", state)

        if config.mode == "build":
            return state

    if config.mode in {"launch", "full"}:
        state = LaunchAgent().run(state)
        state = RetrospectiveAgent().run(state)

    return state


⸻

15. Storage Design

Minimum persistent stores

Run store

Keep:
	•	run_id
	•	mode
	•	niche
	•	created_at
	•	status
	•	artifact paths

Memory store

Keep:
	•	winning niches
	•	failed niches
	•	search patterns
	•	format performance

Use JSON first. Add SQLite when needed.

⸻

16. Error Handling Rules

The system must fail cleanly.

Rules
	•	missing upstream artifact → hard fail
	•	invalid schema parse → hard fail
	•	gate fail → clean terminate with clear reason
	•	model output not parseable → retry once with validator prompt
	•	second parse failure → store raw output and stop

Example pattern:

try:
    parsed = SpendingSignalsReport.model_validate_json(raw)
except Exception:
    repaired = repair_with_validator(raw)
    parsed = SpendingSignalsReport.model_validate_json(repaired)


⸻

17. Tests Required

Minimum tests

Schema tests
	•	every schema validates sample object
	•	every invalid object fails correctly

Gate tests
	•	insufficient spending signals fail
	•	score under 18 fails
	•	missing artifacts fail validation

Orchestrator tests
	•	discover mode stops early
	•	validate mode stops after scoring
	•	full mode writes all expected files

Smoke tests
	•	each agent returns expected artifact key
	•	mock adapter can run end-to-end

⸻

18. README Requirements

The assistant building this should include a README with:
	1.	what KPF is
	2.	supported modes
	3.	install instructions
	4.	.env setup
	5.	example commands
	6.	output structure
	7.	adding a new agent
	8.	adding a new model provider
	9.	validation philosophy
	10.	known limitations

⸻

19. First Build Order

Do not build everything at once.

Phase A
	•	CLI shell
	•	RunConfig schema
	•	Orchestrator skeleton
	•	MockAdapter
	•	IntakeAgent
	•	DiscoveryAgent
	•	SpendingAgent
	•	PainAgent
	•	ScoringAgent
	•	basic gates

Phase B
	•	StrategyAgent
	•	OutlineAgent
	•	DraftingAgent
	•	ArtifactsAgent
	•	ValidationAgent

Phase C
	•	PackagingAgent
	•	LaunchAgent
	•	RetrospectiveAgent
	•	persistence layer
	•	export tools

That sequence matters. Validation comes before polish.

⸻

20. Build Instructions for Another Assistant

Use these exact implementation principles:
	•	schema-first
	•	filesystem-visible outputs
	•	deterministic artifact names
	•	no hidden state
	•	no hand-wavy placeholders in final outputs
	•	all gates explicit
	•	use mockable adapters
	•	optimize for inspectability over cleverness

When uncertain:
	•	prefer simpler architecture
	•	prefer JSON over custom abstractions
	•	prefer explicit pipelines over agent self-routing
	•	prefer hard gates over soft recommendations

⸻

21. Acceptance Criteria

The build is successful only if a user can run:

kpf run validate --niche "therapist insurance credentialing"

and receive:
	•	spending_signals.json
	•	pain_map.json
	•	opportunity_score.json

Then run:

kpf run full --niche "therapist insurance credentialing" --with-personalization

and receive:
	•	product brief
	•	outline
	•	draft product
	•	support artifacts
	•	personalization spec
	•	package manifest
	•	launch assets
	•	validation report

with all outputs saved to a run folder and schema-valid.

⸻

22. Final Instruction to the Builder

Do not optimize for theoretical elegance.

Optimize for:
	•	repeatable runs
	•	easy inspection
	•	strict validation
	•	fast iteration
	•	minimal ambiguity

A blunt, transparent system that rejects bad ideas is more valuable than a clever system that produces polished nonsense.

⸻

Q1

Should I write the copy-paste-ready system prompts for each agent next so another assistant can immediately populate the prompts/ directory?

Q2

Should I define the validation checklist in even stricter operational terms so weak products get blocked automatically?

Q3

Should I turn this into a staged build plan with exact files to create in order, so another assistant can implement KPF step by step without drift?
