from pydantic import BaseModel, Field, NonNegativeInt


class IndexModel(BaseModel):
    index: NonNegativeInt = Field(alias="@index")
