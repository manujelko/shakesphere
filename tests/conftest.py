from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture
from requests import Response


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
def mock_get_fail(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    response = Response()
    response.status_code = 400
    response.url = "fake_url"
    response.reason = "fake_reason"
    mock.return_value.__enter__.return_value = response
    return mock


@pytest.fixture
def mock_post_fail(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.post")
    response = Response()
    response.status_code = 400
    response.url = "fake_url"
    response.reason = "fake_reason"
    mock.return_value.__enter__.return_value = response
    return mock


@pytest.fixture
def mock_post(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.post")
    mock.return_value.__enter__.return_value.json.return_value = {
        "contents": {"translated": "fake_translated_text"},
    }
    return mock
