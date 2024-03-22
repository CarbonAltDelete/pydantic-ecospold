from uuid import UUID

from pydantic import Field, BaseModel, NonNegativeInt

from pyspold.schemas.base.comment import Comment
from pyspold.schemas.base.text import Text


class Geography(BaseModel):
    id: UUID = Field(alias="@id")

    longitude: float | None = Field(alias="@longitude", default=None, lt=180, gt=-180)
    latitude: float | None = Field(alias="@latitude", default=None, lt=90, gt=-90)

    u_n_code: NonNegativeInt | None = Field(alias="@uNCode", default=None)
    u_n_region_code: NonNegativeInt | None = Field(alias="@uNRegionCode", default=None)
    u_n_subregion_code: NonNegativeInt | None = Field(alias="@uNSubregionCode", default=None)

    name: Text
    shortname: Text = Field(alias="shortname")

    comment: Comment | None = None
    kml: None = None
