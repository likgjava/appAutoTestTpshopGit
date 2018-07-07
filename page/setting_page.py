from selenium.webdriver.common.by import By

from page.base_page import BasePage, BaseHandle


class SettingPage(BasePage):
    """
    设置页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 退出按钮
        self.logout_btn = (By.ID, "com.tpshop.malls:id/exit_btn")

    def find_logout_btn(self):
        return self.find_element(self.logout_btn)


class SettingHandle(BaseHandle):
    """
    设置页面-操作层
    """

    def __init__(self):
        self.setting_page = SettingPage()

    def click_logout_btn(self):
        self.setting_page.find_logout_btn().click()


class SettingProxy:
    """
    设置页面-业务层
    """

    def __init__(self):
        self.setting_handle = SettingHandle()

    def logout(self):
        self.setting_handle.click_logout_btn()
