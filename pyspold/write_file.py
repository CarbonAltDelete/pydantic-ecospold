import xmltodict
from pydantic import BaseModel


def write_file(
    file_path: str,
    root: BaseModel,
) -> None:
    with open(file_path, "w") as f:
        f.write(
            xmltodict.unparse(
                root.model_dump(
                    by_alias=True,
                    exclude_none=True,
                ),
                pretty=True,
                short_empty_elements=True,
            ),
        )
