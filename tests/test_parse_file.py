import pyspold

from pyspold.schemas.ecoinvent_root import EcoinventRoot


def test_parse_file():
    file_path = "./data/ecospold_testfile.spold"

    eco_spold = pyspold.parse_file(file_path).eco_spold

    assert eco_spold.xmlns == "http://www.EcoInvent.org/EcoSpold02"


def test_parse_file_with_cls():
    file_path = "./data/ecospold_testfile.spold"

    eco_spold = pyspold.parse_file(
        file_path,
        root_cls=EcoinventRoot,
    ).eco_spold

    assert eco_spold.xmlns == "http://www.EcoInvent.org/EcoSpold02"
