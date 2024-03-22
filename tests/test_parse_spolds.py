import os

import pyspold


def test_parse_spolds():
    folder = "./data/test_spolds"

    for file_path in os.listdir(folder):
        eco_spold = pyspold.parse_file(f"{folder}/{file_path}").eco_spold

        assert eco_spold.xmlns == "http://www.EcoInvent.org/EcoSpold02"

        print(
            "Synonym: ",
            (
                eco_spold.activity_dataset.activity_description.activity.synonyms[0].text
                if eco_spold.activity_dataset.activity_description.activity.synonyms
                else None
            ),
        )
        print(
            "IntermediateExchangeId: ",
            eco_spold.activity_dataset.flow_data.intermediate_exchange.intermediate_exchange_id,
        )
        print("IntermediateExchange", eco_spold.activity_dataset.flow_data.intermediate_exchange.name.text)
