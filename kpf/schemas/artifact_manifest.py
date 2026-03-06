from pydantic import BaseModel


class SupportArtifact(BaseModel):
    name: str
    path: str


class ArtifactManifest(BaseModel):
    artifacts: list[SupportArtifact]
