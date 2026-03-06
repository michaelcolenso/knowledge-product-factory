import typer
from pathlib import Path
from kpf.utils.json_io import read_json

app = typer.Typer(help="Review a run")


@app.command("review")
def review(run_path: str):
    path = Path(run_path) / "validation_report.json"
    if path.exists():
        typer.echo(read_json(path))
    else:
        typer.echo("No validation report found")
