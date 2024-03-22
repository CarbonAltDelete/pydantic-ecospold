from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeInt

from pyspold.schemas.base.text import Text
from pyspold.schemas.geographies.geography import Geography


class ValidGeographies(BaseModel):
    major_release: NonNegativeInt = Field(alias="@majorRelease")
    minor_release: NonNegativeInt = Field(alias="@minorRelease")
    major_revision: NonNegativeInt = Field(alias="@majorRevision")
    minor_revision: NonNegativeInt = Field(alias="@minorRevision")

    context_id: UUID = Field(alias="@contextId")
    xmlns: Literal["http://www.EcoInvent.org/EcoSpold02"] = Field(alias="@xmlns")

    context_name: Text = Field(alias="contextName")

    geographies: list[Geography] = Field(alias="geography")
