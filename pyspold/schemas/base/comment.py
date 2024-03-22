from typing import Any

from pydantic import BaseModel, Field, model_validator

from pyspold.schemas.base.image_url import ImageUrl
from pyspold.schemas.base.indexed_text import IndexedText


class Comment(BaseModel):
    texts: list[IndexedText] = Field(alias="text", default_factory=list)
    image_url: list[ImageUrl] = Field(alias="imageUrl", default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def validate_texts(cls, v: Any) -> Any:
        if v.get("text") and isinstance(v.get("text"), dict):
            v["text"] = [v["text"]]
        return v

    @model_validator(mode="before")
    @classmethod
    def validate_image_urls(cls, v: Any) -> Any:
        if v.get("imageUrl") and isinstance(v.get("imageUrl"), dict):
            v["imageUrl"] = [v["imageUrl"]]
        return v
