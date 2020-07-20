from unittest.mock import Mock

import pytest

from shakesphere.shakespeare import translate


def test_translate(mock_post: Mock) -> None:
    """It gets translated test from the correct keys."""
    translation = translate("fake_text")
    assert translation == "fake_translated_text"


@pytest.mark.integration
def test_translate_integration() -> None:
    """It translated text as expected."""
    text = "This is a normal sentence in contemporary english."
    expected_translation = "This is a ingraft sentence in contemporary english."
    translation = translate(text)
    assert (
        translation == expected_translation
    ), f"Translation expected: {expected_translation}, got: {translation}"
