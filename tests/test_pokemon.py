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
