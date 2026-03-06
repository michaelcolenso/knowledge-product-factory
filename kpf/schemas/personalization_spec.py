from pydantic import BaseModel


class PersonalizationSpec(BaseModel):
    variables: list[str]
    instructions: list[str]
