import pyspold


def test_parse_file():
    file_path = "./data/ecospold_testfile.spold"

    eco_spold = pyspold.parse_file(file_path)

    assert eco_spold.xmlns == "http://www.EcoInvent.org/EcoSpold02"
