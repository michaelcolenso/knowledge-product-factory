"""ArtifactsAgent - creates 3+ support artifacts for the product."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.artifact_manifest import ArtifactManifest


class ArtifactsAgent(BaseAgent):
    name = "artifacts"
    requires: list[str] = ["product_brief", "outline", "draft_product"]

    def _execute(self, state: PipelineState) -> PipelineState:
        brief = state.artifacts["product_brief"]
        outline = state.artifacts["outline"]
        draft = state.artifacts["draft_product"]

        context = (
            f"Product brief: {brief}\n"
            f"Outline: {outline}\n"
            f"Draft (excerpt): {str(draft)[:2000]}"
        )

        # First call: determine what artifacts to create
        raw = self.generate_structured(context, ArtifactManifest)
        manifest = self.parse_with_repair(raw, ArtifactManifest)

        # Second calls: generate each artifact's content
        artifacts_dir = self.run_dir / "product" / "artifacts"
        artifacts_dir.mkdir(parents=True, exist_ok=True)

        system = self.load_prompt("system")
        generate_prompt = self.load_prompt("generate_artifact")

        for item in manifest.items:
            artifact_user = (
                generate_prompt
                + f"\n\nArtifact to create:\nName: {item.name}\nPurpose: {item.purpose}\nFormat: {item.format}"
                + f"\n\nProduct context:\n{brief}"
                + f"\n\nOutline:\n{outline}"
            )
            content = self.adapter.generate(system, artifact_user, temperature=0.3, response_format="text")
            artifact_path = artifacts_dir / item.file_name
            artifact_path.write_text(content, encoding="utf-8")
            self.logger.info(f"Created artifact: {item.file_name}")

        self.write_artifact("artifact_manifest.json", manifest, subdir="product")
        state.artifacts["artifact_manifest"] = self.artifact_dict(manifest)
        state.log(f"ArtifactsAgent: {len(manifest.items)} artifacts created")
        return state
