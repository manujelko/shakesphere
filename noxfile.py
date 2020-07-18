import nox


@nox.session(python=["3.8", "3.7"])
def pytest(session):
    session.install("-e", ".")
    session.install("-r", "requirements/dev.txt")
    session.run("pytest", "--cov", "-m", "not integration")


@nox.session(python=["3.8", "3.7"])
def pytest_integration(session):
    session.install("-e", ".")
    session.install("-r", "requirements/dev.txt")
    session.run("pytest", "-m", "integration")
