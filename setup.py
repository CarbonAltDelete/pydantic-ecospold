from setuptools import setup, find_packages

setup(
    name="pydantic-ecospold",
    version="2024.03.1",
    description="Package to work with Ecoinvent spold files in Python.",
    url="https://github.com/CarbonAltDelete/pydantic-ecospold",
    author="Carbon+Alt+Delete",
    author_email="support@carbonaltdelete.eu",
    license="MIT",
    packages=find_packages(
        include=[
            "pyspold",
            "pyspold.*",
        ],
    ),
    install_requires=[
        "pydantic",
        "xmltodict",
    ],
)
