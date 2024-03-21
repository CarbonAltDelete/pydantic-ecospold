from uuid import UUID

from pydantic import BaseModel, Field

from pyspold.schemas.base.comment import Comment
from pyspold.schemas.base.short_name import ShortName


class Geography(BaseModel):
    geography_id: UUID = Field(alias="@geographyId")
    short_name: ShortName = Field(alias="shortname")
    comment: Comment | None = None
