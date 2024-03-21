import pyspold


def test_write_file():
    file_path = "./data/ecospold_testfile.spold"

    eco_spold = pyspold.parse_file(file_path)

    assert eco_spold.xmlns == "http://www.EcoInvent.org/EcoSpold02"

    pyspold.write_file(f"{file_path[:-6]}_[WRITE].spold", eco_spold)
