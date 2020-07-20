from typing import Dict

from bottle import Bottle
from requests.exceptions import HTTPError

from .pokemon import get_random_pokemon_description
from .shakespeare import translate


app = Bottle()


@app.route("/pokemon/<pokemon_name>")
def poke_translation(pokemon_name: str) -> Dict[str, str]:
    """Endpoint yielding Shakespearean Pokemon descriptions."""
    try:
        description = get_random_pokemon_description(pokemon_name)
        translation = translate(description)
        output = {"name": pokemon_name, "description": translation}
        return output
    except HTTPError as http_err:
        return {"error": str(http_err)}
