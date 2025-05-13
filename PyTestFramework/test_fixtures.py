import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixture(self):
        print("I am executing steps in test fixture method")

    def test_fixture1(self):
        print("I am executing steps in test fixture method")

    def test_fixture2(self):
        print("I am executing steps in test fixture method")

