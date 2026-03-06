"""kpf run subcommands."""

from pathlib import Path

import typer
from rich.console import Console

from kpf.logger import configure_root_logger
from kpf.models import get_adapter
from kpf.orchestrator.engine import PipelineEngine
from kpf.orchestrator.state import PipelineState
from kpf.schemas.run_config import Constraints, RunConfig
from kpf.settings import get_settings

run_app = typer.Typer(help="Run knowledge product factory pipelines")
console = Console()


def _build_adapter(model: str, dry_run: bool):
    if dry_run:
        from kpf.models.mock_adapter import MockAdapter
        return MockAdapter()
    settings = get_settings()
    return get_adapter(model, settings)


def _run_with_orchestrator(config: RunConfig, model: str, dry_run: bool, orchestrator: str) -> PipelineState:
    """Run pipeline via the specified orchestrator."""
    if orchestrator == "agent":
        import os
        settings = get_settings()
        # Support both KPF_ANTHROPIC_API_KEY and the standard ANTHROPIC_API_KEY
        api_key = settings.anthropic_api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        if not api_key:
            console.print("[bold red]Error:[/bold red] Set ANTHROPIC_API_KEY or KPF_ANTHROPIC_API_KEY for --orchestrator agent")
            raise typer.Exit(1)
        inner_adapter = _build_adapter(model, dry_run)
        from kpf.orchestrator.agent_orchestrator import AgentOrchestrator
        orch = AgentOrchestrator(anthropic_api_key=api_key, inner_adapter=inner_adapter)
        return orch.run(config)
    else:
        adapter = _build_adapter(model, dry_run)
        engine = PipelineEngine()
        return engine.run(config, adapter)


def _display_result(state: PipelineState) -> None:
    console.print(f"\n[bold green]Run complete:[/bold green] {state.run_id}")
    if state.run_dir:
        console.print(f"[dim]Output:[/dim] {state.run_dir}")
    console.print(f"[dim]Artifacts:[/dim] {', '.join(state.artifacts.keys())}")
    gates_passed = [k for k, v in state.gates.items() if v]
    if gates_passed:
        console.print(f"[dim]Gates passed:[/dim] {', '.join(gates_passed)}")


@run_app.command("discover")
def discover(
    model: str = typer.Option("anthropic", "--model", "-m", help="Model adapter to use"),
    temperature: float = typer.Option(0.2, "--temperature", "-t", help="LLM temperature"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Use mock adapter (no API calls)"),
    output_dir: Path | None = typer.Option(None, "--output-dir", help="Override output directory"),
) -> None:
    """Discover knowledge product niches without a specific niche in mind."""
    configure_root_logger()
    config = RunConfig(mode="discover", constraints=Constraints())
    adapter = _build_adapter(model, dry_run)
    engine = PipelineEngine()
    state = engine.run(config, adapter)
    _display_result(state)


@run_app.command("validate")
def validate(
    niche: str = typer.Argument(..., help="The niche to validate"),
    max_weeks: int = typer.Option(3, "--max-weeks", help="Max creation weeks"),
    price_floor: int = typer.Option(79, "--price-floor", help="Minimum price USD"),
    price_ceiling: int = typer.Option(199, "--price-ceiling", help="Maximum price USD"),
    model: str = typer.Option("anthropic", "--model", "-m"),
    temperature: float = typer.Option(0.2, "--temperature", "-t"),
    dry_run: bool = typer.Option(False, "--dry-run"),
    strict: bool = typer.Option(True, "--strict/--no-strict", help="Enforce strict gates"),
    orchestrator: str = typer.Option("engine", "--orchestrator", "-o", help="Orchestrator: engine (default) or agent"),
) -> None:
    """Validate a specific niche with spending, pain, and opportunity scoring."""
    configure_root_logger()
    config = RunConfig(
        mode="validate",
        niche=niche,
        strict_mode=strict,
        model=model,
        temperature=temperature,
        constraints=Constraints(
            max_creation_weeks=max_weeks,
            price_floor=price_floor,
            price_ceiling=price_ceiling,
        ),
    )
    state = _run_with_orchestrator(config, model, dry_run, orchestrator)
    _display_result(state)


@run_app.command("build")
def build(
    brief: Path = typer.Argument(..., help="Path to product_brief.json"),
    model: str = typer.Option("anthropic", "--model", "-m"),
    temperature: float = typer.Option(0.2, "--temperature", "-t"),
    dry_run: bool = typer.Option(False, "--dry-run"),
) -> None:
    """Build a product from an existing product brief."""
    configure_root_logger()
    import json
    brief_data = json.loads(brief.read_text())
    niche = brief_data.get("opportunity_name", "")
    config = RunConfig(mode="build", niche=niche, model=model, temperature=temperature)
    adapter = _build_adapter(model, dry_run)
    engine = PipelineEngine()

    from kpf.utils.files import make_run_id
    from kpf.paths import RUNS_DIR
    from kpf.orchestrator.state import PipelineState

    run_id = make_run_id(niche)
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    state = PipelineState(run_id=run_id, mode="build", niche=niche, run_dir=run_dir)
    state.artifacts["run_config"] = config.model_dump()
    state.artifacts["product_brief"] = brief_data

    state = engine._run_pipeline(state, config, adapter)
    _display_result(state)


@run_app.command("launch")
def launch(
    product_dir: Path = typer.Argument(..., help="Path to product run directory"),
    model: str = typer.Option("anthropic", "--model", "-m"),
    dry_run: bool = typer.Option(False, "--dry-run"),
) -> None:
    """Create launch assets for an existing validated product."""
    configure_root_logger()
    console.print(f"[bold]Launching from:[/bold] {product_dir}")
    config = RunConfig(mode="launch", model=model)
    adapter = _build_adapter(model, dry_run)
    engine = PipelineEngine()
    state = engine.run(config, adapter)
    _display_result(state)


@run_app.command("full")
def full(
    niche: str = typer.Argument(..., help="The niche to build a full product for"),
    with_personalization: bool = typer.Option(False, "--with-personalization", help="Include personalization"),
    formats: str = typer.Option(
        "playbook,template_library,notion_system",
        "--formats",
        help="Comma-separated allowed formats",
    ),
    max_weeks: int = typer.Option(3, "--max-weeks"),
    price_floor: int = typer.Option(79, "--price-floor"),
    price_ceiling: int = typer.Option(199, "--price-ceiling"),
    model: str = typer.Option("anthropic", "--model", "-m"),
    temperature: float = typer.Option(0.2, "--temperature", "-t"),
    dry_run: bool = typer.Option(False, "--dry-run"),
    strict: bool = typer.Option(True, "--strict/--no-strict"),
    orchestrator: str = typer.Option("engine", "--orchestrator", "-o", help="Orchestrator: engine (default) or agent"),
) -> None:
    """Run the complete pipeline from validation through launch."""
    configure_root_logger()
    format_list = [f.strip() for f in formats.split(",")]
    config = RunConfig(
        mode="full",
        niche=niche,
        with_personalization=with_personalization,
        strict_mode=strict,
        model=model,
        temperature=temperature,
        constraints=Constraints(
            max_creation_weeks=max_weeks,
            price_floor=price_floor,
            price_ceiling=price_ceiling,
            allowed_formats=format_list,
        ),
    )
    state = _run_with_orchestrator(config, model, dry_run, orchestrator)
    _display_result(state)
