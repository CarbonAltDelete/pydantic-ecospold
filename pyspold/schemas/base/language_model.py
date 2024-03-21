from typing import Literal

from pydantic import BaseModel, Field


class LanguageModel(BaseModel):
    language: Literal["en"] = Field(alias="@xml:lang")
