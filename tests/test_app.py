from unittest.mock import Mock

import pytest
from webtest import TestApp

from shakesphere.app import app as myapp
from shakesphere.app import poke_translation


def test_poke_translation(mock_get: Mock, mock_post: Mock) -> None:
    result = poke_translation("fake_pokemon")
    assert result == {"name": "fake_pokemon", "description": "fake_translated_text"}


@pytest.mark.e2e
def test_app() -> None:
    app = TestApp(myapp)
    pokemon_name = "charizard"
    response = app.get(f"/pokemon/{pokemon_name}")
    assert response.status == "200 OK"
