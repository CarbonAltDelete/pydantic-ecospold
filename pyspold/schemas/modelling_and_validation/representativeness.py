from uuid import UUID

from pydantic import BaseModel, Field

from pyspold.schemas.base.text import Text


class Representativeness(BaseModel):
    system_model_id: UUID = Field(alias="@systemModelId")
    sampling_procedure: Text | None = Field(alias="samplingProcedure", default=None)
    extrapolations: Text | None = Field(alias="extrapolations", default=None)
