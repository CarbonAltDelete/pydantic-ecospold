from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeInt

from pyspold.schemas.activity_description.activity_name import ActivityName
from pyspold.schemas.base.comment import Comment
from pyspold.schemas.base.text import Text


class Activity(BaseModel):
    id: UUID = Field(alias="@id")
    special_activity_type: NonNegativeInt = Field(alias="@specialActivityType")
    activity_name: ActivityName = Field(alias="activityName")
    general_comment: Comment | None = Field(alias="generalComment", default=None)
    included_activities_start: Text | None = Field(
        alias="includedActivitiesStart",
        default=None,
    )
    included_activities_end: Text | None = Field(
        alias="includedActivitiesEnd",
        default=None,
    )
