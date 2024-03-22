from typing import TypeVar

import xmltodict
from pydantic import BaseModel

from pyspold.schemas.ecoinvent_root import EcoinventRoot

T = TypeVar("T", bound=BaseModel)


def parse_file(
    file_path: str,
    root_cls: type[T] = EcoinventRoot,
) -> T:
    with open(file_path, "r") as f:
        return root_cls.model_validate(xmltodict.parse(f.read()))
