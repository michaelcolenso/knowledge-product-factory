"""PackagingAgent - creates the buyer-facing package manifest."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.package_manifest import PackageManifest


class PackagingAgent(BaseAgent):
    name = "packaging"
    requires: list[str] = ["draft_product", "artifact_manifest", "product_brief"]

    def _execute(self, state: PipelineState) -> PipelineState:
        brief = state.artifacts["product_brief"]
        artifact_manifest = state.artifacts["artifact_manifest"]
        context = f"Product brief: {brief}\nArtifacts: {artifact_manifest}"

        raw = self.generate_structured(context, PackageManifest)
        manifest = self.parse_with_repair(raw, PackageManifest)

        self.write_artifact("package_manifest.json", manifest, subdir="package")
        state.artifacts["package_manifest"] = self.artifact_dict(manifest)
        state.log(f"PackagingAgent: {len(manifest.included_files)} files in package")
        return state
