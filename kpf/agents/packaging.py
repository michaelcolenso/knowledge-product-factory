from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.package_manifest import PackageManifest
from kpf.utils.json_io import write_json


class PackagingAgent(BaseAgent):
    name = "packaging"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        manifest = PackageManifest(
            product_files=[
                "product_brief.json",
                "outline.json",
                "knowledge_base.json",
                "draft_product.md",
                "artifact_manifest.json",
            ],
            launch_files=[],
            version="v0.1.0",
        )
        path = state.run_dir / "package_manifest.json"
        write_json(path, manifest.model_dump())
        state.data["package_manifest"] = manifest
        state.register_artifact("package_manifest", path)
        return state
