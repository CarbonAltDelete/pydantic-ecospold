from uuid import UUID

from pydantic import BaseModel, Field

from pyspold.schemas.base.text import Text


class Classification(BaseModel):
    classification_id: UUID = Field(alias="@classificationId")
    classification_value: Text = Field(alias="classificationValue")
    classification_system: Text = Field(alias="classificationSystem")
