import pytest

from shakesphere.pokemon import get_descriptions, get_pokemon_species_url


@pytest.fixture
def mock_species_url(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "species": {"url": "Totally fake url"},
    }
    return mock


@pytest.fixture
def mock_descriptions(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "flavor_text_entries": [
            {"flavor_text": "fake description english", "language": {"name": "en"}},
            {"flavor_text": " fake description italian", "language": {"name": "it"}},
        ]
    }
    return mock


def test_get_pokemon_species_url(mock_species_url) -> None:
    url = get_pokemon_species_url("fake pokemon")
    assert url == "Totally fake url"


def test_get_descriptions(mock_descriptions) -> None:
    descriptions = get_descriptions("fake url")
    assert descriptions[0] == "fake description english"


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
    url = get_pokemon_species_url(pokemon_name)
    assert (
        url == expected_url
    ), f"Unexpected url found: {url}, {expected_url} was expected"


@pytest.mark.integration
@pytest.mark.parametrize(
    "url",
    [
        pytest.param("https://pokeapi.co/api/v2/pokemon-species/25/"),
        pytest.param("https://pokeapi.co/api/v2/pokemon-species/1/"),
        pytest.param("https://pokeapi.co/api/v2/pokemon-species/7/"),
        pytest.param("https://pokeapi.co/api/v2/pokemon-species/4/"),
    ],
    ids=["pikachu", "bulbasaur", "squirtle", "charmander"],
)
def test_get_descriptions_integration(url):
    descriptions = get_descriptions(url)
    assert descriptions, f"Expected a list of descriptions, got {descriptions}"
