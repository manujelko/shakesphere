import random
from typing import List

import requests

API = "https://pokeapi.co/api/v2/pokemon/"


def get_random_pokemon_description(pokemon_name: str) -> str:
    """Retrieve one of the available descriptions for the given pokemon.

    Args:
        pokemon_name: pokemon of interest.

    Returns:
        pokemon description.
    """
    return random.choice(get_descriptions(get_pokemon_species_url(pokemon_name)))


def get_pokemon_species_url(pokemon_name: str) -> str:
    """Retrieve url for pokemon species.

    Args:
        pokemon_name: pokemon of interest.

    Returns:
        url containing pokemon descriptions.
    """
    endpoint = f"{API}{pokemon_name}"
    with requests.get(endpoint) as response:
        response.raise_for_status()
        url: str = response.json()["species"]["url"]
    return url


def get_descriptions(url: str) -> List[str]:
    """Retrieve available (english) descriptions from the given url.

    Args:
        url: url containing the pokemon descriptions.

    Returns:
        list of available pokemon descriptions.
    """
    with requests.get(url) as response:
        response.raise_for_status()
        all_descriptions = response.json()["flavor_text_entries"]
        uniq_en_descriptions = [
            description["flavor_text"]
            for description in all_descriptions
            if description["language"]["name"] == "en"
        ]
        return list(uniq_en_descriptions)
