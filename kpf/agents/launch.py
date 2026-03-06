from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import OrchestratorState
from kpf.schemas.launch_assets import LaunchAssets
from kpf.utils.files import write_text
from kpf.utils.json_io import write_json


class LaunchAgent(BaseAgent):
    name = "launch"

    def run(self, state: OrchestratorState) -> OrchestratorState:
        launch_dir = state.run_dir / "launch"
        assets = {
            "sales_page.md": "# Sales Page\nGet credentialed faster.\n",
            "gumroad_listing.md": "# Gumroad Listing\nIncludes playbook and templates.\n",
            "faq.md": "# FAQ\nQ: Who is this for?\n",
            "objections.md": "# Objections\nI am too busy.\n",
            "launch_posts.md": "# Launch Posts\nPost 1...\n",
        }
        for fname, content in assets.items():
            write_text(launch_dir / fname, content)
        model = LaunchAssets(**{k.split('.')[0]: str((launch_dir / k).relative_to(state.run_dir)) for k in assets})
        path = state.run_dir / "launch_assets.json"
        write_json(path, model.model_dump())
        state.data["launch_assets"] = model
        state.register_artifact("launch_assets", path)
        return state
