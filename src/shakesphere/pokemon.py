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
        url = response.json()["species"]["url"]
    return url
