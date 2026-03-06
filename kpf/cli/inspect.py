import typer
from pathlib import Path

app = typer.Typer(help="Inspect run artifacts")


@app.command("inspect")
def inspect_run(run_path: str):
    p = Path(run_path)
    for f in sorted(p.rglob("*")):
        if f.is_file():
            typer.echo(f.relative_to(p))
