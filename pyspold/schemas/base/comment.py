from pydantic import BaseModel, Field

from pyspold.schemas.base.image_url import ImageUrl
from pyspold.schemas.base.indexed_text import IndexedText


class Comment(BaseModel):
    texts: list[IndexedText] | IndexedText | None = Field(alias="text", default=None)
    image_url: list[ImageUrl] | ImageUrl | None = Field(alias="imageUrl", default=None)
