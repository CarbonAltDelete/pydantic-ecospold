from pydantic import BaseModel, Field, NonNegativeInt


class FileAttributes(BaseModel):
    major_release: NonNegativeInt = Field(alias="@majorRelease")
    minor_release: NonNegativeInt = Field(alias="@minorRelease")
    major_revision: NonNegativeInt = Field(alias="@majorRevision")
    minor_revision: NonNegativeInt = Field(alias="@minorRevision")
