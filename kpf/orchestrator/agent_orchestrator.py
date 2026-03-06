"""Agent-based pipeline orchestrator.

Instead of a hardcoded sequential engine, Claude acts as the orchestrator.
Each pipeline stage is exposed as a tool Claude can call. Claude reads gate
results and adapts — stopping cleanly on gate failures, skipping phases based
on mode, and explaining decisions in natural language.
"""

import json
from pathlib import Path

import anthropic
from anthropic import beta_tool

from kpf.logger import get_logger
from kpf.models.adapter_base import ModelAdapter
from kpf.orchestrator.state import PipelineState
from kpf.paths import RUNS_DIR
from kpf.schemas.run_config import RunConfig
from kpf.utils.files import make_run_id
from kpf.utils.json_io import write_json

logger = get_logger("agent_orchestrator")

_SYSTEM_PROMPT = """You are the Knowledge Product Factory (KPF) orchestrator. You execute a multi-stage pipeline to research, validate, and build knowledge products.

## Pipeline Stages

**Validation Phase** (validate / full modes):
1. run_spending_analysis — evidence people pay to solve this problem
2. check_spending_gate — require 3+ signals, 2+ with dollar/time amounts
3. run_pain_mapping — specific recurring pain and its consequences
4. check_pain_gate — require specific question, workarounds, and quantified cost
5. run_competitor_analysis — map alternatives and their weaknesses
6. run_opportunity_scoring — score 5 dimensions (max 25 total)
7. check_score_gate — require total ≥ 18 and decision = CREATE

**Build Phase** (build / full modes, only after validation passes):
8. run_strategy — product brief: format, price, promise, channels
9. run_outline — section-level structure
10. run_synthesis — structured knowledge base from all research
11. run_drafting — full long-form product draft
12. run_artifacts — 3+ support files (checklists, templates, CSVs)
13. run_packaging — buyer-facing package manifest

**Launch Phase** (full / launch modes):
14. run_validation — final quality check (PASS / REVISE / FAIL)
15. run_launch — launch assets (only if validation = PASS)
16. run_retrospective — postmortem and memory updates

## Mode Stopping Points
- discover: return niche candidates only (no tools needed)
- validate: stop after step 7
- build: stop after step 13
- full: run all 16 steps
- launch: start from step 14

## Gate Rules
- If a gate returns FAIL, stop immediately with a clear explanation
- Never proceed to build if score < 18 or decision ≠ CREATE
- Never proceed to launch if validation ≠ PASS

Report each gate result (PASS or FAIL with reason). Be explicit about which stage you are running and why.
"""


class AgentOrchestrator:
    """Orchestrates the KPF pipeline using Claude as the decision-maker.

    The orchestrator model (Claude Opus) receives the full pipeline as tools
    and decides the execution order based on mode, gate results, and failures.
    Each tool internally delegates to the same KPF agents used by PipelineEngine,
    but the sequencing and gate logic is now driven by the model.
    """

    def __init__(self, anthropic_api_key: str, inner_adapter: ModelAdapter) -> None:
        self.client = anthropic.Anthropic(api_key=anthropic_api_key)
        self.inner_adapter = inner_adapter

    def run(self, config: RunConfig) -> PipelineState:
        run_id = make_run_id(config.niche)
        run_dir = RUNS_DIR / run_id
        run_dir.mkdir(parents=True, exist_ok=True)

        state = PipelineState(
            run_id=run_id,
            mode=config.mode,
            niche=config.niche,
            run_dir=run_dir,
        )

        # Seed run_config so agents can read constraints
        state.artifacts["run_config"] = config.model_dump()

        tools = self._build_tools(state, run_dir)
        user_prompt = self._build_user_prompt(config)

        logger.info(f"Agent orchestrator starting: mode={config.mode}, niche={config.niche}")

        runner = self.client.beta.messages.tool_runner(
            model="claude-opus-4-6",
            max_tokens=8192,
            thinking={"type": "adaptive"},
            system=_SYSTEM_PROMPT,
            tools=tools,
            messages=[{"role": "user", "content": user_prompt}],
        )

        for message in runner:
            logger.debug(f"Orchestrator turn: {type(message).__name__}")

        write_json(
            run_dir / "summary.json",
            {
                "run_id": state.run_id,
                "mode": state.mode,
                "niche": state.niche,
                "artifact_keys": list(state.artifacts.keys()),
                "gates": state.gates,
                "orchestrator": "agent",
            },
        )

        return state

    # ------------------------------------------------------------------
    # Prompt
    # ------------------------------------------------------------------

    def _build_user_prompt(self, config: RunConfig) -> str:
        niche = f'"{config.niche}"' if config.niche else "(discover — no niche specified)"
        return (
            f"Run the KPF pipeline in **{config.mode.upper()}** mode for niche: {niche}\n\n"
            f"Constraints:\n"
            f"- Max creation weeks: {config.constraints.max_creation_weeks}\n"
            f"- Price range: ${config.constraints.price_floor}–${config.constraints.price_ceiling}\n"
            f"- Allowed formats: {', '.join(config.constraints.allowed_formats)}\n"
            f"- With personalization: {config.with_personalization}\n\n"
            f"Execute the pipeline stages for {config.mode.upper()} mode. "
            f"Stop at the appropriate point and report the final status."
        )

    # ------------------------------------------------------------------
    # Tool construction
    # ------------------------------------------------------------------

    def _build_tools(self, state: PipelineState, run_dir: Path) -> list:
        """Build beta_tool functions closed over shared mutable state."""
        inner = self.inner_adapter

        def _run(agent_class: type) -> PipelineState:
            agent = agent_class(adapter=inner, run_dir=run_dir)
            result = agent.run(state)
            state.artifacts.update(result.artifacts)
            state.logs.extend(result.logs)
            return result

        def _gate(enforce_fn, gate_name: str) -> str:
            from kpf.orchestrator.gates import GateError
            try:
                enforce_fn(state)
                return f"PASS: {gate_name} gate passed."
            except GateError as e:
                state.gates[e.gate] = False
                return f"FAIL: {e.reason}"

        # ---- Validation phase ----------------------------------------

        @beta_tool
        def run_spending_analysis(niche: str) -> str:
            """Synthesize spending signals — evidence people pay to solve this problem.

            Args:
                niche: The specific niche to analyze (e.g. 'therapist insurance credentialing').
            """
            from kpf.agents.spending import SpendingAgent
            state.niche = niche
            _run(SpendingAgent)
            signals = state.artifacts.get("spending_signals", {})
            count = signals.get("signal_count", 0)
            passes = signals.get("passes_threshold", False)
            return f"Found {count} spending signals. passes_threshold={passes}.\n{json.dumps(signals, indent=2)}"

        @beta_tool
        def check_spending_gate() -> str:
            """Check spending gate: requires 3+ signals with 2+ quantified dollar/time costs."""
            from kpf.orchestrator.gates import enforce_spending_gate
            return _gate(enforce_spending_gate, "spending")

        @beta_tool
        def run_pain_mapping(niche: str) -> str:
            """Map the specific recurring pain, consequences, and current workarounds.

            Args:
                niche: The niche to map pain for.
            """
            from kpf.agents.pain import PainAgent
            _run(PainAgent)
            pain = state.artifacts.get("pain_map", {})
            return f"Pain mapped. Core question: {pain.get('core_question', 'N/A')}\n{json.dumps(pain, indent=2)}"

        @beta_tool
        def check_pain_gate() -> str:
            """Check pain gate: requires specific question, current workarounds, quantified consequences."""
            from kpf.orchestrator.gates import enforce_pain_gate
            return _gate(enforce_pain_gate, "pain")

        @beta_tool
        def run_competitor_analysis(niche: str) -> str:
            """Map existing alternatives and their weaknesses.

            Args:
                niche: The niche to map competitors for.
            """
            from kpf.agents.competitors import CompetitorsAgent
            _run(CompetitorsAgent)
            cmap = state.artifacts.get("competitor_map", {})
            count = len(cmap.get("alternatives", []))
            return f"Found {count} alternatives.\n{json.dumps(cmap, indent=2)}"

        @beta_tool
        def run_opportunity_scoring() -> str:
            """Score the opportunity across 5 dimensions. Total >= 18 required to proceed."""
            from kpf.agents.scoring import ScoringAgent
            _run(ScoringAgent)
            score = state.artifacts.get("opportunity_score", {})
            return (
                f"Score: {score.get('total')}/25  Decision: {score.get('decision')}  "
                f"Confidence: {score.get('confidence')}\n{json.dumps(score, indent=2)}"
            )

        @beta_tool
        def check_score_gate() -> str:
            """Check score gate: requires total >= 18 and decision = CREATE."""
            from kpf.orchestrator.gates import enforce_score_gate
            result = _gate(enforce_score_gate, "score")
            if result.startswith("PASS"):
                score = state.artifacts.get("opportunity_score", {})
                return f"{result} Total={score.get('total')}, Decision={score.get('decision')}"
            return result

        # ---- Build phase ---------------------------------------------

        @beta_tool
        def run_strategy() -> str:
            """Design the product brief: format, core promise, price, differentiator, distribution."""
            from kpf.agents.strategy import StrategyAgent
            _run(StrategyAgent)
            brief = state.artifacts.get("product_brief", {})
            return (
                f"Product brief: {brief.get('opportunity_name')} | "
                f"Format: {brief.get('format')} | Price: ${brief.get('price')}\n"
                f"{json.dumps(brief, indent=2)}"
            )

        @beta_tool
        def run_outline() -> str:
            """Create the section-level product outline based on the product brief."""
            from kpf.agents.outline import OutlineAgent
            _run(OutlineAgent)
            outline = state.artifacts.get("outline", {})
            sections = len(outline.get("sections", []))
            return f"Outline: {outline.get('product_title')} — {sections} sections"

        @beta_tool
        def run_synthesis() -> str:
            """Build a structured knowledge base synthesized from all upstream research."""
            from kpf.agents.synthesis import SynthesisAgent
            _run(SynthesisAgent)
            kb = state.artifacts.get("knowledge_base", {})
            return (
                f"Knowledge base: {len(kb.get('facts', []))} facts, "
                f"{len(kb.get('decisions', []))} decisions, "
                f"{len(kb.get('pitfalls', []))} pitfalls"
            )

        @beta_tool
        def run_drafting() -> str:
            """Write the full product draft as long-form markdown following the outline."""
            from kpf.agents.drafting import DraftingAgent
            _run(DraftingAgent)
            draft = str(state.artifacts.get("draft_product", ""))
            return f"Draft written: {len(draft):,} characters → {run_dir}/product/draft_product.md"

        @beta_tool
        def run_artifacts() -> str:
            """Create 3+ support artifacts (checklists, templates, CSV spreadsheets)."""
            from kpf.agents.artifacts import ArtifactsAgent
            _run(ArtifactsAgent)
            manifest = state.artifacts.get("artifact_manifest", {})
            items = manifest.get("items", [])
            names = [i.get("file_name", "?") for i in items]
            return f"Created {len(items)} artifacts: {', '.join(names)}"

        @beta_tool
        def run_packaging() -> str:
            """Create the buyer-facing package manifest listing all included files."""
            from kpf.agents.packaging import PackagingAgent
            _run(PackagingAgent)
            pkg = state.artifacts.get("package_manifest", {})
            return (
                f"Package: {pkg.get('product_name')} v{pkg.get('version')} ({pkg.get('tier')}) — "
                f"{len(pkg.get('included_files', []))} files"
            )

        # ---- Launch phase -------------------------------------------

        @beta_tool
        def run_validation() -> str:
            """Run final quality validation. Returns PASS, REVISE, or FAIL with specific issues."""
            from kpf.agents.validation import ValidationAgent
            _run(ValidationAgent)
            report = state.artifacts.get("validation_report", {})
            status = report.get("status", "UNKNOWN")
            issues = report.get("issues", [])
            revisions = report.get("required_revisions", [])
            parts = [f"Validation: {status}"]
            if issues:
                parts.append(f"Issues: {'; '.join(issues)}")
            if revisions:
                parts.append(f"Required revisions: {'; '.join(str(r) for r in revisions[:3])}")
            return " | ".join(parts)

        @beta_tool
        def run_launch() -> str:
            """Create all launch assets: sales page, Gumroad listing, FAQ, objections, launch posts.
            Only call this if validation returned PASS."""
            from kpf.agents.launch import LaunchAgent
            from kpf.orchestrator.gates import enforce_launch_gate, GateError
            try:
                enforce_launch_gate(state)
            except GateError as e:
                return f"BLOCKED — cannot launch: {e.reason}"
            _run(LaunchAgent)
            assets = state.artifacts.get("launch_assets", {})
            posts = len(assets.get("launch_posts", []))
            return f"Launch assets created: sales page, Gumroad listing, FAQ, objections, {posts} posts → {run_dir}/launch/"

        @beta_tool
        def run_retrospective() -> str:
            """Write postmortem and update memory files (winning/failed niches, format performance)."""
            from kpf.agents.retrospective import RetrospectiveAgent
            _run(RetrospectiveAgent)
            return f"Postmortem written → {run_dir}/postmortem.json. Memory files updated."

        return [
            run_spending_analysis,
            check_spending_gate,
            run_pain_mapping,
            check_pain_gate,
            run_competitor_analysis,
            run_opportunity_scoring,
            check_score_gate,
            run_strategy,
            run_outline,
            run_synthesis,
            run_drafting,
            run_artifacts,
            run_packaging,
            run_validation,
            run_launch,
            run_retrospective,
        ]
