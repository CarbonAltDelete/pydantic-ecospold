import pyspold


def test_write_file():
    file_path = "./data/ecospold_testfile.spold"

    eco_root = pyspold.parse_file(file_path)

    assert eco_root.eco_spold.xmlns == "http://www.EcoInvent.org/EcoSpold02"

    pyspold.write_file(f"{file_path[:-6]}_[WRITE].spold", eco_root)

    eco_root2 = pyspold.parse_file(f"{file_path[:-6]}_[WRITE].spold")

    assert eco_root == eco_root2
