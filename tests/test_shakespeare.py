import pytest

from shakesphere.shakespeare import translate


@pytest.fixture
def mock_requests(mocker):
    mock = mocker.patch("requests.post")
    mock.return_value.__enter__.return_value.json.return_value = {
        "contents": {"translated": "fake_translated_text"},
    }
    return mock


def test_translate(mock_requests) -> None:
    translation = translate("fake_text")
    assert translation == "fake_translated_text"


@pytest.mark.integration
def test_translate_integration() -> None:
    text = "This is a normal sentence in contemporary english."
    expected_translation = "This is a ingraft sentence in contemporary english."
    translation = translate(text)
    assert (
        translation == expected_translation
    ), f"Translation expected: {expected_translation}, got: {translation}"
