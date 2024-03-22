import pyspold
from pyspold.schemas.geography_root import GeographyRoot


def test_parse_geographies():
    file_path = "./data/Geographies.xml"

    root = pyspold.parse_file(file_path, root_cls=GeographyRoot)

    print(f"\nGeographies: {root.valid_geographies.geographies[0]}")

    pyspold.write_file(f"{file_path[:-4]}_[WRITE].xml", root)

    root2 = pyspold.parse_file(f"{file_path[:-4]}_[WRITE].xml", root_cls=GeographyRoot)

    assert root == root2
