from pydantic import BaseModel, Field

from pyspold.schemas.flow_data.impact_indicator import ImpactIndicator
from pyspold.schemas.flow_data.intermediate_exchange import IntermediateExchange


class FlowData(BaseModel):
    intermediate_exchange: IntermediateExchange = Field(alias="intermediateExchange")
    impact_indicators: list[ImpactIndicator] = Field(alias="impactIndicator")
