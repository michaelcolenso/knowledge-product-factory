from pydantic import BaseModel


class PackageManifest(BaseModel):
    product_files: list[str]
    launch_files: list[str]
    version: str
