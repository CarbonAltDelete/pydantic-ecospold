from pydantic import BaseModel, Field

from pyspold.schemas.modelling_and_validation.representativeness import Representativeness


class ModellingAndValidation(BaseModel):
    representativeness: Representativeness = Field(alias="representativeness")
