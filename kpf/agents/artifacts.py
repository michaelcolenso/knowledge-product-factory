from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.artifact_manifest import ArtifactManifest, SupportArtifact
from kpf.utils.files import write_text
from kpf.utils.json_io import write_json


class ArtifactsAgent(BaseAgent):
    name = "artifacts"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        root = state.run_dir / "artifacts"
        files = {
            "credentialing_checklist.md": "# Credentialing Checklist\n- Prep\n- Submit\n- Follow-up\n",
            "revenue_calculator.csv": "clients,rate,revenue\n10,120,1200\n",
            "followup_email_scripts.md": "# Follow-up scripts\nTemplate A\n",
        }
        items = []
        for name, content in files.items():
            path = root / name
            write_text(path, content)
            items.append(SupportArtifact(name=name, path=str(path.relative_to(state.run_dir))))
        manifest = ArtifactManifest(artifacts=items)
        mpath = state.run_dir / "artifact_manifest.json"
        write_json(mpath, manifest.model_dump())
        state.data["artifact_manifest"] = manifest
        state.register_artifact("artifact_manifest", mpath)
        return state
