import nox

@nox.session(name="tests-3.11", python="3.11")
def test_311(session):
    session.install("pytest")
    session.run("pytest")

@nox.session(name="tests-3.12", python="3.12")
def test_312(session):
    session.install("pytest")
    session.run("pytest")

@nox.session(name="tests-3.13", python="3.13")
def test_313(session):
    session.install("pytest")
    session.run("pytest")
