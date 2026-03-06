import typer
from kpf.cli.run import app as run_app
from kpf.cli.review import app as review_app
from kpf.cli.inspect import app as inspect_app
from kpf.cli.export import app as export_app

app = typer.Typer(help="KPF CLI")
app.add_typer(run_app, name="run")
app.add_typer(review_app)
app.add_typer(inspect_app)
app.add_typer(export_app)

if __name__ == "__main__":
    app()
