# Any pytest file should start or end with test_ or _test
# Pytest method should start with "test" keyword.
# Code should be wrapped in method only
import pytest as pytest


# If you want to pass from the Command prompt... Copy the path of the Folder. in Cmd use this. cd path name
# "py.test" command will be helpful to run all the tests present in the Path Specified.
# "py.test -v" command will be used to get the more information about the test cases Executed "V" stands for verbos.
# "py.test -v -s" command will be used to get the information of Console logs also.
# if two methods have same name , while executing it will override the previous method and returns the latest method.
# Two different files can have same methods as in the First file data

@pytest.mark.smoke
@pytest.mark.xfail
def test_first_program():
    msg = "Hello"
    assert msg == "Hello", "Match failed"


def test_second_program():
    a = 2
    b = 4
    print(a)
    print(b)


def test_cross_browser(cross_browser):
    print(cross_browser[1])
