from pydantic import Field

from pyspold.schemas.base.language_model import LanguageModel


class TextModel(LanguageModel):
    text: str = Field(alias="#text", default="")
