import pytest

from shakesphere.pokemon import (
    get_descriptions,
    get_pokemon_species_url,
    get_random_pokemon_description,
)


@pytest.fixture
def mock_requests(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "species": {"url": "fake_species_url"},
        "flavor_text_entries": [
            {"flavor_text": "fake_description_en", "language": {"name": "en"}},
            {"flavor_text": "fake_description_it", "language": {"name": "it"}},
        ],
    }


def test_get_pokemon_species_url(mock_requests) -> None:
    """It gets the url from the correct key."""
    url = get_pokemon_species_url("fake_pokemon")
    assert url == "fake_species_url"


def test_get_descriptions(mock_requests) -> None:
    """It gets the descriptions in english."""
    descriptions = get_descriptions("fake_url")
    assert descriptions[0] == "fake_description_en"


def test_get_random_pokemon_description(mock_requests) -> None:
    """It gets a description."""
    description = get_random_pokemon_description("fake_pokemon")
    assert description == "fake_description_en"


@pytest.mark.integration
@pytest.mark.parametrize(
    "pokemon_name, expected_url",
    [
        pytest.param("pikachu", "https://pokeapi.co/api/v2/pokemon-species/25/"),
        pytest.param("bulbasaur", "https://pokeapi.co/api/v2/pokemon-species/1/"),
        pytest.param("squirtle", "https://pokeapi.co/api/v2/pokemon-species/7/"),
        pytest.param("charmander", "https://pokeapi.co/api/v2/pokemon-species/4/"),
    ],
)
def test_get_pokemon_species_url_integration(pokemon_name, expected_url) -> None:
    """It gets the expected urls."""
    url = get_pokemon_species_url(pokemon_name)
    assert (
        url == expected_url
    ), f"Unexpected url found: {url}, {expected_url} was expected"


@pytest.mark.integration
@pytest.mark.parametrize(
    "url",
    [
        "https://pokeapi.co/api/v2/pokemon-species/25/",
        "https://pokeapi.co/api/v2/pokemon-species/1/",
        "https://pokeapi.co/api/v2/pokemon-species/7/",
        "https://pokeapi.co/api/v2/pokemon-species/4/",
    ],
    ids=["pikachu", "bulbasaur", "squirtle", "charmander"],
)
def test_get_descriptions_integration(url) -> None:
    """It gets a list of descriptions."""
    descriptions = get_descriptions(url)
    assert descriptions, "Expected a list of descriptions"


@pytest.mark.integration
@pytest.mark.parametrize(
    "pokemon_name", ["pikachu", "bulbasaur", "squirtle", "charmander"]
)
def test_get_random_pokemon_description_integration(pokemon_name) -> None:
    """It gets a description."""
    description = get_random_pokemon_description(pokemon_name)
    assert description, "Expected a pokemon description"
