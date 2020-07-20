import nox
from nox.sessions import Session

nox.options.sessions = "lint", "mypy", "pytest"
locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.8", "3.7"])
def pytest(session: Session) -> None:
    """Run unit tests and ensure coverage is 100 %."""
    session.install("-e", ".")
    session.install("-r", "requirements.txt")
    session.install("pytest", "pytest-mock", "pytest-cov", "webtest")
    session.run("pytest", "--cov", "-m", "not integration and not e2e")


@nox.session(python=["3.8", "3.7"])
def integration(session: Session) -> None:
    """Run integration tests."""
    session.install("-e", ".")
    session.install("-r", "requirements.txt")
    session.install("pytest", "pytest_mock", "webtest")
    session.run("pytest", "-m", "integration")


@nox.session(python=["3.8", "3.7"])
def e2e(session: Session) -> None:
    """Run end-to-end tests."""
    session.install("-e", ".")
    session.install("-r", "requirements.txt")
    session.install("pytest", "pytest_mock", "webtest")
    session.run("pytest", "-m", "e2e")


@nox.session(python=["3.8", "3.7"])
def lint(session: Session) -> None:
    """Lint with flake8."""
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session: Session) -> None:
    """Format code with black."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.8", "3.7"])
def mypy(session: Session) -> None:
    """Run static type-checking with mypy."""
    args = session.posargs or locations
    session.install("-e", ".")
    session.install("-r", "requirements.txt")
    session.install("mypy")
    session.run("mypy", *args)
