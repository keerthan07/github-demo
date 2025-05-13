import pytest


@pytest.fixture(scope="class")
def setup():
    print("I am executing First")
    yield
    print("I will be executing last")


@pytest.fixture()
def data():
    print("The profile details")
    return ["Keerthan", "Sharma", "keerthan98@gmail.com"]


@pytest.fixture(params=[("Chrome", "Keerthan"), ("Firefox", "Sharma"), ("IE", "Rampalli")])
def cross_browser(request):
    return request.param
