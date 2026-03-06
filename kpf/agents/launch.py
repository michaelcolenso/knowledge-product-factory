"""LaunchAgent - creates all launch marketing assets."""

from kpf.agents.base import BaseAgent
from kpf.orchestrator.state import PipelineState
from kpf.schemas.launch_assets import LaunchAssets


class LaunchAgent(BaseAgent):
    name = "launch"
    requires: list[str] = ["product_brief", "package_manifest", "validation_report"]

    def _execute(self, state: PipelineState) -> PipelineState:
        brief = state.artifacts["product_brief"]
        pkg = state.artifacts["package_manifest"]
        pain = state.artifacts.get("pain_map", {})

        context = (
            f"Product brief: {brief}\n"
            f"Package manifest: {pkg}\n"
            f"Pain map: {pain}"
        )

        raw = self.generate_structured(context, LaunchAssets)
        assets = self.parse_with_repair(raw, LaunchAssets)

        # Write individual launch files
        launch_dir = self.run_dir / "launch"
        launch_dir.mkdir(parents=True, exist_ok=True)

        (launch_dir / "sales_page.md").write_text(assets.sales_page_md, encoding="utf-8")
        (launch_dir / "gumroad_listing.md").write_text(assets.gumroad_listing_md, encoding="utf-8")
        (launch_dir / "faq.md").write_text(assets.faq_md, encoding="utf-8")
        (launch_dir / "objections.md").write_text(assets.objections_md, encoding="utf-8")
        (launch_dir / "launch_posts.md").write_text(
            "\n\n---\n\n".join(assets.launch_posts), encoding="utf-8"
        )
        (launch_dir / "lead_magnet.md").write_text(assets.lead_magnet_concept, encoding="utf-8")

        state.artifacts["launch_assets"] = self.artifact_dict(assets)
        state.log(f"LaunchAgent: {len(assets.launch_posts)} launch posts created")
        return state
