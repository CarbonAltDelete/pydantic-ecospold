from pydantic import Field

from pyspold.schemas.base.index_model import IndexModel


class ImageUrl(IndexModel):
    text: str = Field(alias="#text", default="")
