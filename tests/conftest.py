from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture


def pytest_configure(config):
    config.addinivalue_line("markers", "integration: mark as integration tests")
    config.addinivalue_line("markers", "e2e: mark as integration tests")


@pytest.fixture
def mock_get(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "species": {"url": "fake_species_url"},
        "flavor_text_entries": [
            {"flavor_text": "fake_description_en", "language": {"name": "en"}},
            {"flavor_text": "fake_description_it", "language": {"name": "it"}},
        ],
    }
    return mock


@pytest.fixture
def mock_post(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.post")
    mock.return_value.__enter__.return_value.json.return_value = {
        "contents": {"translated": "fake_translated_text"},
    }
    return mock
