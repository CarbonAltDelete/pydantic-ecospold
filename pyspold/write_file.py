import xmltodict

from pyspold.schemas.eco_spold import EcoSpold
from pyspold.schemas.ecoinvent_root import EcoinventRoot


def write_file(file_path: str, eco_spold: EcoSpold) -> None:
    with open(file_path, "w") as f:
        root = EcoinventRoot(eco_spold=eco_spold)
        f.write(xmltodict.unparse(root.model_dump(by_alias=True), pretty=True))
