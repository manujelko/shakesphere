import requests


API = "https://api.funtranslations.com/translate/shakespeare.json"


def translate(text: str) -> str:
    request_data = {"text": text}
    with requests.post(API, data=request_data) as response:
        translated_text = response.json()["contents"]["translated"]
    return translated_text
