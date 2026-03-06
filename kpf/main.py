"""KPF CLI entry point."""

import typer

from kpf.cli.run import run_app
from kpf.cli.review import review
from kpf.cli.inspect import inspect
from kpf.cli.export import export

app = typer.Typer(
    name="kpf",
    help="Knowledge Product Factory - create validated, schema-first knowledge products.",
    no_args_is_help=True,
)

app.add_typer(run_app, name="run")
app.command("review")(review)
app.command("inspect")(inspect)
app.command("export")(export)


if __name__ == "__main__":
    app()
