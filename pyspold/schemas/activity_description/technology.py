from pydantic import BaseModel, Field, NonNegativeInt

from pyspold.schemas.base.comment import Comment


class Technology(BaseModel):
    technology_level: NonNegativeInt | None = Field(
        alias="@technologyLevel",
        default=None,
    )
    comment: Comment | None = None
