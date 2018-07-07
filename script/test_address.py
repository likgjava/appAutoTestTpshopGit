import allure
import pytest
from selenium.common.exceptions import TimeoutException

from common import utils
from page.add_address_page import AddAddressProxy
from page.address_page import AddressProxy
from page.login_page import LoginProxy
from page.main_page import MainProxy
from page.mine_page import MineProxy
from page.setting_page import SettingProxy
from common.utils import DriverUtil
from common.utils import YamlUtil


def build_address_data():
    # return [
    #     ("13041092162", "tpshop12345678", "登录成功"),
    #     ("13041092162", "tpshop1234567", "密码错误"),
    #     ("1301234", "tpshop12345678", "账号不存在")
    # ]
    data = YamlUtil.get_data_by_key("address", "test_address")
    print(data)
    data_list = []
    for login in data.values():
        # name,mobile,province,city,district,town,address
        data_list.append((login["name"], login["mobile"], login["province"],
                          login["city"], login["district"], login["town"],
                          login["address"], login["toast"]))
    print("data_list=", data_list)
    return data_list



class TestAddress:

    @classmethod
    def setup_class(cls):
        print('setup_class')
        cls.main_proxy = MainProxy()
        cls.mine_proxy = MineProxy()
        cls.login_proxy = LoginProxy()
        cls.setting_proxy = SettingProxy()
        cls.address_proxy = AddressProxy()
        cls.add_address_proxy = AddAddressProxy()

    # @classmethod
    # def teardown_class(cls):
    #     print('teardown_class')
    #     DriverUtil.quit_driver()

    def setup(self):
        # 进入‘我的’页面
        self.main_proxy.to_mine_page()

        # 进入‘收货地址’页面
        self.mine_proxy.to_address_page()

    def teardown(self):
        print('teardown')
        # self.login_proxy.back_to_mine_page()

    @allure.step("新增收货地址")
    @pytest.mark.parametrize("name,mobile,province,city,district,town,address,toast", build_address_data())
    def test_address(self, name, mobile, province, city, district, town, address, toast):
        # print("test_address username={} password={} toast={}".format(username, password, toast))
        # allure.attach("用例参数：", "username={} password={} toast={}".format(username, password, toast))

        # 点击‘新建地址’
        self.address_proxy.to_add_address_page()

        self.add_address_proxy.add_address(name, mobile, province, city, district, town, address)

        assert utils.is_exist_toast(toast)
