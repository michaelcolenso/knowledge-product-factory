"""Mock adapter for testing - returns fixture JSON without LLM calls."""

import json
from pathlib import Path


FIXTURES_DIR = Path(__file__).parent.parent.parent / "tests" / "fixtures"

SCHEMA_FIXTURES: dict[str, str] = {
    "NicheCandidateList": "niche_candidate_list.json",
    "SpendingSignalsReport": "spending_signals_report.json",
    "PainMap": "pain_map.json",
    "CompetitorMap": "competitor_map.json",
    "OpportunityScore": "opportunity_score.json",
    "ProductBrief": "product_brief.json",
    "Outline": "outline.json",
    "KnowledgeBase": "knowledge_base.json",
    "ArtifactManifest": "artifact_manifest.json",
    "PersonalizationSpec": "personalization_spec.json",
    "PackageManifest": "package_manifest.json",
    "ValidationReport": "validation_report.json",
    "LaunchAssets": "launch_assets.json",
}


def _extract_schema_hint(user_prompt: str) -> str | None:
    marker = "<!-- schema_hint:"
    if marker in user_prompt:
        start = user_prompt.index(marker) + len(marker)
        end = user_prompt.index("-->", start)
        return user_prompt[start:end].strip()
    return None


class MockAdapter:
    """Returns deterministic fixture JSON for testing. No LLM calls."""

    def __init__(self, fixtures_dir: Path | None = None) -> None:
        self.fixtures_dir = fixtures_dir or FIXTURES_DIR
        self.calls: list[dict[str, str]] = []

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        response_format: str = "text",
    ) -> str:
        self.calls.append(
            {
                "system": system_prompt[:100],
                "user": user_prompt[:100],
                "temperature": str(temperature),
                "response_format": response_format,
            }
        )

        if response_format == "text":
            return "Mock text response."

        hint = _extract_schema_hint(user_prompt)
        if hint and hint in SCHEMA_FIXTURES:
            fixture_path = self.fixtures_dir / SCHEMA_FIXTURES[hint]
            if fixture_path.exists():
                return fixture_path.read_text()

        return json.dumps({"mock": "response", "hint": hint})
