from uuid import UUID

from pydantic import BaseModel, Field

from pyspold.schemas.base.text import Text


class ImpactIndicator(BaseModel):
    impact_indicator_id: UUID = Field(alias="@impactIndicatorId")
    impact_method_id: UUID = Field(alias="@impactMethodId")
    impact_category_id: UUID = Field(alias="@impactCategoryId")
    amount: float = Field(alias="@amount")
    impact_method_name: Text | str = Field(alias="impactMethodName")
    impact_category_name: Text | str = Field(alias="impactCategoryName")
    name: Text | str = Field(alias="name")
    unit_name: Text | str = Field(alias="unitName")
