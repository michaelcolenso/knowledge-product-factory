import typer
from kpf.orchestrator.engine import run_pipeline
from kpf.schemas.run_config import RunConfig

app = typer.Typer(help="Run KPF pipeline modes")


@app.command("discover")
def discover(max_weeks: int = typer.Option(3, "--max-weeks"), model: str = typer.Option("mock", "--model")):
    run_pipeline(RunConfig(mode="discover", max_weeks=max_weeks, model_provider=model))


@app.command("validate")
def validate(
    niche: str = typer.Option(..., "--niche"),
    max_weeks: int = typer.Option(3, "--max-weeks"),
    min_score: int = typer.Option(18, "--min-score"),
    model: str = typer.Option("mock", "--model"),
):
    run_pipeline(RunConfig(mode="validate", niche=niche, max_weeks=max_weeks, min_score=min_score, model_provider=model))


@app.command("build")
def build(
    brief: str = typer.Option(..., "--brief"),
    with_personalization: bool = typer.Option(False, "--with-personalization"),
    model: str = typer.Option("mock", "--model"),
):
    run_pipeline(RunConfig(mode="build", niche="from_brief", brief=brief, with_personalization=with_personalization, model_provider=model))


@app.command("launch")
def launch(
    product: str = typer.Option(..., "--product"),
    niche: str = typer.Option("launch-product", "--niche"),
    model: str = typer.Option("mock", "--model"),
):
    run_pipeline(RunConfig(mode="launch", product=product, niche=niche, model_provider=model))


@app.command("full")
def full(
    niche: str = typer.Option(..., "--niche"),
    max_weeks: int = typer.Option(3, "--max-weeks"),
    min_score: int = typer.Option(18, "--min-score"),
    with_personalization: bool = typer.Option(False, "--with-personalization"),
    model: str = typer.Option("mock", "--model"),
):
    run_pipeline(RunConfig(mode="full", niche=niche, max_weeks=max_weeks, min_score=min_score, with_personalization=with_personalization, model_provider=model))
