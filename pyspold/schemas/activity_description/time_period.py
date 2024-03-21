import datetime

from pydantic import BaseModel, Field

from pyspold.schemas.base.comment import Comment


class TimePeriod(BaseModel):
    is_data_valid_for_entire_period: bool = Field(alias="@isDataValidForEntirePeriod")
    start_date: datetime.date = Field(alias="@startDate")
    end_date: datetime.date = Field(alias="@endDate")
    comment: Comment | None = None
