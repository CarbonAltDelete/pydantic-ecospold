from pydantic import BaseModel, Field, ConfigDict

from pyspold.schemas.eco_spold import EcoSpold


class EcoinventRoot(BaseModel):
    eco_spold: EcoSpold = Field(alias="ecoSpold")

    model_config = ConfigDict(
        populate_by_name=True,
    )
