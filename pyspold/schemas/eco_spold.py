from typing import Literal

from pydantic import BaseModel, Field, AliasChoices

from pyspold.schemas.activity_dataset import ActivityDataset


class EcoSpold(BaseModel):
    xmlns: Literal["http://www.EcoInvent.org/EcoSpold02"] = Field(alias="@xmlns")
    xmlns_xsi: Literal["http://www.w3.org/2001/XMLSchema-instance"] | None = Field(
        alias="@xmlns:xsi",
        default=None,
    )
    activity_dataset: ActivityDataset = Field(
        alias=AliasChoices(
            "childActivityDataset",
            "activityDataset",
        ),
    )
