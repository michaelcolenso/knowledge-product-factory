"""kpf export command - export run artifacts."""

import shutil
import zipfile
from pathlib import Path

import typer
from rich.console import Console

console = Console()


def export(
    run_dir: Path = typer.Argument(..., help="Path to run directory"),
    format: str = typer.Option("zip", "--format", "-f", help="Export format: zip, markdown"),
    output: Path | None = typer.Option(None, "--output", "-o", help="Output path"),
) -> None:
    """Export run artifacts to a distributable format."""
    if not run_dir.exists():
        console.print(f"[red]Run directory not found:[/red] {run_dir}")
        raise typer.Exit(1)

    if format == "zip":
        out_path = output or Path(f"{run_dir.name}.zip")
        with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in run_dir.rglob("*"):
                if f.is_file():
                    zf.write(f, f.relative_to(run_dir.parent))
        console.print(f"[green]Exported to:[/green] {out_path}")

    elif format == "markdown":
        out_dir = output or Path(f"{run_dir.name}_export")
        out_dir.mkdir(parents=True, exist_ok=True)
        for f in run_dir.rglob("*.md"):
            dest = out_dir / f.name
            shutil.copy2(f, dest)
        console.print(f"[green]Markdown files exported to:[/green] {out_dir}")

    elif format == "pdf":
        raise typer.BadParameter("PDF export requires pandoc. Install with: apt install pandoc")

    else:
        raise typer.BadParameter(f"Unknown format: {format}. Use: zip, markdown")
