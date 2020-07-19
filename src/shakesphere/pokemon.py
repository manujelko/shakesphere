from typing import List

import requests

API = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_species_url(pokemon_name: str) -> str:
    """Retrieve url for pokemon species.

    Args:
        pokemon_name: pokemon of interest.

    Returns:
        url containing pokemon descriptions.
    """
    endpoint = f"{API}{pokemon_name}"
    with requests.get(endpoint) as response:
        url: str = response.json()["species"]["url"]
    return url


def get_descriptions(url: str) -> List[str]:
    with requests.get(url) as response:
        all_descriptions = response.json()["flavor_text_entries"]
        uniq_en_descriptions = [
            description["flavor_text"]
            for description in all_descriptions
            if description["language"]["name"] == "en"
        ]
        return list(uniq_en_descriptions)
