from uuid import UUID

from pydantic import BaseModel, Field

from pyspold.schemas.base.text import Text


class IntermediateExchange(BaseModel):
    id: UUID = Field(alias="@id")
    intermediate_exchange_id: UUID = Field(alias="@intermediateExchangeId")
    unit_name: Text = Field(alias="unitName")
    name: Text
