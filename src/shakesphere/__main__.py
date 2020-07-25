import sys

from bottle import run

from .app import app


if __name__ == "__main__":
    if len(sys.argv) == 1:
        run(app, host="localhost", port=8080)
    elif len(sys.argv) == 2 and sys.argv[1] == "--docker":
        run(app, host="0.0.0.0", port=8000)
    else:
        raise RuntimeError("--docker is the only allowed argument")
