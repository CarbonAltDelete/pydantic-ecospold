from pydantic import BaseModel, Field

from pyspold.schemas.geographies.valid_geographies import ValidGeographies


class GeographyRoot(BaseModel):
    valid_geographies: ValidGeographies = Field(alias="validGeographies")
