import pytest

from shakesphere.pokemon import get_pokemon_species_url


@pytest.fixture
def mock_species_url(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "species": {"url": "Totally fake url"},
    }
    return mock


def test_get_pokemon_species_url(mock_species_url) -> None:
    url = get_pokemon_species_url("fake pokemon")
    assert url == "Totally fake url"


@pytest.mark.integration
@pytest.mark.parametrize("pokemon_name, expected_url", [
    pytest.param("pikachu", "https://pokeapi.co/api/v2/pokemon-species/25/"),
    pytest.param("bulbasaur", "https://pokeapi.co/api/v2/pokemon-species/1/"),
    pytest.param("squirtle", "https://pokeapi.co/api/v2/pokemon-species/7/"),
    pytest.param("charmander", "https://pokeapi.co/api/v2/pokemon-species/4/"),
])
def test_get_pokemon_species_url_integration(pokemon_name, expected_url) -> None:
    url = get_pokemon_species_url(pokemon_name)
    assert url == expected_url, f"Unexpected url found: {url}, {expected_url} was expected"
