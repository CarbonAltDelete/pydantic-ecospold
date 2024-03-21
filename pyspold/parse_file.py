import xmltodict

from pyspold.schemas.eco_spold import EcoSpold
from pyspold.schemas.ecoinvent_root import EcoinventRoot


def parse_file(file_path: str) -> EcoSpold:
    with open(file_path, "r") as f:
        root = EcoinventRoot.model_validate(xmltodict.parse(f.read()))

    return root.eco_spold
