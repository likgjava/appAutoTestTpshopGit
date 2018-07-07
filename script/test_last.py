import pytest

from common.utils import DriverUtil


@pytest.mark.last
class TestLast:

    @classmethod
    def teardown_class(cls):
        print('TestLast.teardown_class')
        DriverUtil.quit_driver()

    def test_last(self):
        print("收尾处理")
