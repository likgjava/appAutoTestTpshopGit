import allure
import pytest
from selenium.common.exceptions import TimeoutException

from common import utils
from page.login_page import LoginProxy
from page.main_page import MainProxy
from page.mine_page import MineProxy
from page.setting_page import SettingProxy
from common.utils import DriverUtil
from common.utils import YamlUtil


def is_exist_text(driver, text):
    """
    判断页面中是否存在指定的文本内容
    :param driver: 驱动对象
    :param text: 文本内容
    :return: 存在返回True，不存在返回False
    """
    try:
        xpath = "//*[contains(@text, '{}')]".format(text)
        ele = driver.find_element_by_xpath(xpath)
        print("ele=====", ele)
        return ele is not None
    except TimeoutException:
        print("not find toast={}".format(text))
        return False


def build_login_data():
    # return [
    #     ("13041092162", "tpshop12345678", "登录成功"),
    #     ("13041092162", "tpshop1234567", "密码错误"),
    #     ("1301234", "tpshop12345678", "账号不存在")
    # ]
    data = YamlUtil.get_data_by_key("login", "test_login")
    print(data)
    data_list = []
    for login in data.values():
        data_list.append((login["username"], login["password"], login["toast"]))
    print("data_list=", data_list)
    return data_list


@pytest.mark.run(order=1)
class TestLogin:

    @classmethod
    def setup_class(cls):
        print('setup_class')
        cls.main_proxy = MainProxy()
        cls.mine_proxy = MineProxy()
        cls.login_proxy = LoginProxy()
        cls.setting_proxy = SettingProxy()

    # @classmethod
    # def teardown_class(cls):
    #     print('teardown_class')
    #     DriverUtil.quit_driver()

    def setup(self):
        # 进入‘我的’页面
        self.main_proxy.to_mine_page()

        # 如果是已登录状态，则要先退出
        is_login = self.mine_proxy.is_login()
        print("is_login=", is_login)
        if is_login:
            self.mine_proxy.to_setting_page()
            self.setting_proxy.logout()

        # 进入‘登录’页面
        self.mine_proxy.to_login_page()

    def teardown(self):
        print('teardown')
        # 如果是登录页面，则返回到‘我的’页面
        is_login_page = self.login_proxy.is_login_page()
        if is_login_page:
            self.login_proxy.back_to_mine_page()

    @allure.step("登录功能")
    @pytest.mark.parametrize("username,password,toast", build_login_data())
    def test_login(self, username, password, toast):
        print("test_login username={} password={} toast={}".format(username, password, toast))
        allure.attach("用例参数：", "username={} password={} toast={}".format(username, password, toast))

        self.login_proxy.login(username, password)

        # 截图
        png = DriverUtil.get_driver().get_screenshot_as_png()
        allure.attach("截图", png, allure.attach_type.PNG)

        assert utils.is_exist_toast(toast)
