from pydantic import BaseModel, Field

from pyspold.schemas.activity_description.activity import Activity
from pyspold.schemas.activity_description.classification import Classification
from pyspold.schemas.activity_description.geography import Geography
from pyspold.schemas.activity_description.macro_economic_scenario import MacroEconomicScenario
from pyspold.schemas.activity_description.technology import Technology
from pyspold.schemas.activity_description.time_period import TimePeriod


class ActivityDescription(BaseModel):
    activity: Activity
    geography: Geography
    classifications: list[Classification] | Classification | None = Field(
        alias="classification",
        default=None,
    )
    technology: Technology | None = Field(alias="technology")
    time_period: TimePeriod = Field(alias="timePeriod")
    macro_economic_scenario: MacroEconomicScenario = Field(
        alias="macroEconomicScenario",
    )
