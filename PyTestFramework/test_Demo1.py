# Any pytest file should start or end with test_ or _test
# Pytest method should start with "test" keyword.
# Code should be wrapped in method only
import pytest


# If you want to pass from the Command prompt... Copy the path of the Folder. in Cmd use this. cd path name
# "py.test" command will be helpful to run all the tests present in the Path Specified.
# "py.test -v" command will be used to get the more information about the test cases Executed "V" stands for verbos.
# "py.test -v -s" command will be used to get the information of Console logs also.
# if two methods have same name , while executing it will override the previous method and returns the latest method.
# if you want to run only a particular file "py.test test_Demo2.py -v -s" use this command
# in middle we should use the file name
# Fixtures are used as setup and teardown methods for test cases  -  conftest  file to generalize fixtures and make
# it available to all test cases

@pytest.mark.smoke
@pytest.mark.skip
def test_first_program():
    print("Hello")


def test_second_program():
    print("Good Morning")
