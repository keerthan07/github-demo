import pytest

from PyTestFramework.Baseclass import BaseClass


@pytest.mark.usefixtures("data")
class TestData(BaseClass):

    def test_edit_profile(self, data):
        log = self.get_logger()

        log.info(data[1])

