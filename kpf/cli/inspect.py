"""kpf inspect command - deep inspection of a run directory."""

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

console = Console()


def inspect(
    run_dir: Path = typer.Argument(..., help="Path to run directory"),
) -> None:
    """Deep inspection of gates, logs, and validation for a run."""
    if not run_dir.exists():
        console.print(f"[red]Run directory not found:[/red] {run_dir}")
        raise typer.Exit(1)

    summary_path = run_dir / "summary.json"
    if summary_path.exists():
        import orjson
        summary = orjson.loads(summary_path.read_bytes())
        console.print(Panel(
            f"[bold]Run ID:[/bold] {summary.get('run_id')}\n"
            f"[bold]Mode:[/bold] {summary.get('mode')}\n"
            f"[bold]Niche:[/bold] {summary.get('niche')}\n"
            f"[bold]Artifacts:[/bold] {', '.join(summary.get('artifact_keys', []))}\n"
            f"[bold]Gates:[/bold] {summary.get('gates')}",
            title="Run Summary",
        ))

    validation_path = run_dir / "validation_report.json"
    if validation_path.exists():
        import orjson
        report = orjson.loads(validation_path.read_bytes())
        status = report.get("status", "UNKNOWN")
        color = "green" if status == "PASS" else "red"
        console.print(Panel(
            f"[bold]Status:[/bold] [{color}]{status}[/{color}]\n"
            f"[bold]Checks:[/bold] {report.get('checks')}\n"
            f"[bold]Issues:[/bold] {report.get('issues')}\n"
            f"[bold]Required revisions:[/bold] {report.get('required_revisions')}",
            title="Validation Report",
        ))

    score_path = run_dir / "niche_analysis" / "opportunity_score.json"
    if score_path.exists():
        import orjson
        score = orjson.loads(score_path.read_bytes())
        console.print(Panel(
            f"[bold]Total:[/bold] {score.get('total')}/25\n"
            f"[bold]Decision:[/bold] {score.get('decision')}\n"
            f"[bold]Confidence:[/bold] {score.get('confidence')}\n"
            f"[bold]Scores:[/bold] {score.get('scores')}",
            title="Opportunity Score",
        ))
