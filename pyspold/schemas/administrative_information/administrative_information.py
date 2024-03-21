from pydantic import BaseModel, Field

from pyspold.schemas.administrative_information.file_attributes import FileAttributes


class AdministrativeInformation(BaseModel):
    file_attributes: FileAttributes = Field(alias="fileAttributes")
