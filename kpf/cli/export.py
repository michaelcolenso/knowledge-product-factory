import typer
from pathlib import Path

app = typer.Typer(help="Export run artifacts")


@app.command("export")
def export_run(run_path: str, format: str = "pdf"):
    out = Path(run_path) / f"export.{format}"
    out.write_text("KPF export artifact", encoding="utf-8")
    typer.echo(str(out))
