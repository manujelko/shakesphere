import nox

nox.options.sessions = "lint", "pytest"
locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.8", "3.7"])
def pytest(session):
    session.install("-e", ".")
    session.install("-r", "requirements.txt")
    session.install("pytest", "pytest-mock", "pytest-cov")
    session.run("pytest", "--cov", "-m", "not integration")


@nox.session(python=["3.8", "3.7"])
def integration(session):
    session.install("-e", ".")
    session.install("-r", "requirements.txt")
    session.install("pytest")
    session.run("pytest", "-m", "integration")


@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.8", "3.7"])
def mypy(session):
    args = session.posargs or locations
    session.install("-e", ".")
    session.install("-r", "requirements.txt")
    session.install("mypy")
    session.run("mypy", *args)
