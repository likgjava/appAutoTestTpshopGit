from selenium.webdriver.common.by import By

from page.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """
    登录页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 账号
        self.user_name = (By.ID, "com.tpshop.malls:id/edit_phone_num")
        # 密码
        self.password = (By.ID, "com.tpshop.malls:id/edit_password")
        # 登录按钮
        self.login_btn = (By.ID, "com.tpshop.malls:id/btn_login")
        # 返回按钮
        self.back_btn = (By.ID, "com.tpshop.malls:id/titlebar_back_rl")

    def find_user_name(self):
        return self.find_element(self.user_name)

    def find_password(self):
        return self.find_element(self.password)

    def find_login_btn(self):
        return self.find_element(self.login_btn)

    def find_back_btn(self):
        return self.find_element(self.back_btn)


class LoginHandle(BaseHandle):
    """
    登录页面-操作层
    """

    def __init__(self):
        self.login_page = LoginPage()

    def input_user_name(self, user_name):
        self.send_keys(self.login_page.find_user_name(), user_name)

    def input_password(self, password):
        self.send_keys(self.login_page.find_password(), password)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()

    def click_back_btn(self):
        self.login_page.find_back_btn().click()

    def exist_login_btn(self):
        try:
            element = self.login_page.find_login_btn()
            return element is not None
        except Exception:
            return False


class LoginProxy:
    """
    登录页面-业务层
    """

    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, user_name, password):
        self.login_handle.input_user_name(user_name)
        self.login_handle.input_password(password)
        self.login_handle.click_login_btn()

    def back_to_mine_page(self):
        self.login_handle.click_back_btn()

    def is_login_page(self):
        return self.login_handle.exist_login_btn()
