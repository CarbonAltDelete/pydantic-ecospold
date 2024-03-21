from uuid import UUID

from pydantic import BaseModel, Field

from pyspold.schemas.base.text import Text


class MacroEconomicScenario(BaseModel):
    macro_economic_scenario_id: UUID = Field(alias="@macroEconomicScenarioId")
    name: Text = Field(alias="name")
