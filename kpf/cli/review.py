"""kpf review command - display run artifacts in a table."""

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

console = Console()


def review(
    run_dir: Path = typer.Argument(..., help="Path to run directory"),
) -> None:
    """Review artifacts in a run directory."""
    if not run_dir.exists():
        console.print(f"[red]Run directory not found:[/red] {run_dir}")
        raise typer.Exit(1)

    table = Table(title=f"Run: {run_dir.name}", show_header=True)
    table.add_column("File", style="cyan")
    table.add_column("Size", justify="right")
    table.add_column("Valid", justify="center")

    for f in sorted(run_dir.rglob("*")):
        if f.is_file() and not f.name.startswith("."):
            size = f"{f.stat().st_size:,} B"
            valid = "-"
            if f.suffix == ".json":
                try:
                    import orjson
                    orjson.loads(f.read_bytes())
                    valid = "[green]✓[/green]"
                except Exception:
                    valid = "[red]✗[/red]"

            rel_path = f.relative_to(run_dir)
            table.add_row(str(rel_path), size, valid)

    console.print(table)
