"""ValidationAgent - enforces all quality gates and produces validation report."""

from kpf.agents.base import BaseAgent
from kpf.config import MIN_ARTIFACTS
from kpf.orchestrator.state import PipelineState
from kpf.schemas.artifact_manifest import ArtifactManifest
from kpf.schemas.validation_report import ValidationReport


class ValidationAgent(BaseAgent):
    name = "validation"
    requires: list[str] = ["draft_product", "artifact_manifest", "package_manifest"]

    def _execute(self, state: PipelineState) -> PipelineState:
        checks: dict[str, bool] = {}
        issues: list[str] = []

        # Check draft exists and has content
        draft = state.artifacts.get("draft_product", "")
        checks["draft_exists"] = bool(draft and len(str(draft)) > 500)
        if not checks["draft_exists"]:
            issues.append("Draft product is missing or too short (< 500 chars)")

        # Check artifact count
        manifest_raw = state.artifacts.get("artifact_manifest", {})
        manifest = ArtifactManifest.model_validate(manifest_raw)
        checks["sufficient_artifacts"] = len(manifest.items) >= MIN_ARTIFACTS
        if not checks["sufficient_artifacts"]:
            issues.append(f"Only {len(manifest.items)} support artifacts, need {MIN_ARTIFACTS}+")

        # Check package manifest exists
        checks["package_manifest_exists"] = "package_manifest" in state.artifacts
        if not checks["package_manifest_exists"]:
            issues.append("Package manifest is missing")

        # Check product brief has required fields
        brief = state.artifacts.get("product_brief", {})
        checks["has_target_user"] = bool(brief.get("target_user", ""))
        checks["has_distribution"] = bool(brief.get("distribution_channels", []))
        checks["has_price"] = bool(brief.get("price", 0))
        if not checks["has_target_user"]:
            issues.append("Product brief missing target_user")
        if not checks["has_distribution"]:
            issues.append("Product brief missing distribution_channels")

        # Determine status
        critical_checks = ["draft_exists", "sufficient_artifacts", "package_manifest_exists"]
        if all(checks.get(c, False) for c in critical_checks):
            if issues:
                status = "REVISE"
            else:
                status = "PASS"
        else:
            status = "FAIL"

        # Use LLM for qualitative issues list if status is not FAIL
        required_revisions: list[str] = []
        if status == "REVISE":
            context = (
                f"Draft excerpt: {str(draft)[:1000]}\n"
                f"Issues found: {issues}\n"
                f"Product brief: {brief}"
            )
            system = self.load_prompt("system")
            task = self.load_prompt("task")
            qualitative = self.adapter.generate(
                system,
                task + f"\n\nContext:\n{context}",
                temperature=0.1,
                response_format="text",
            )
            required_revisions = [qualitative.strip()]

        report = ValidationReport(
            status=status,
            checks=checks,
            issues=issues,
            required_revisions=required_revisions,
        )

        self.write_artifact("validation_report.json", report)
        state.artifacts["validation_report"] = self.artifact_dict(report)
        state.log(f"ValidationAgent: status={report.status}, {len(issues)} issues")
        return state
