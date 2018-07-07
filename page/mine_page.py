from selenium.webdriver.common.by import By

from page.base_page import BasePage, BaseHandle


class MinePage(BasePage):
    """
    我的页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 登录/注册
        self.login_btn = (By.ID, "com.tpshop.malls:id/nickname_txtv")
        # 设置按钮
        self.setting_btn = (By.ID, "com.tpshop.malls:id/setting_btn")
        # 收货地址
        self.address = (By.XPATH, "//*[@text='收货地址']")

    def find_login_btn(self):
        return self.find_element(self.login_btn)

    def find_setting_btn(self):
        return self.find_element(self.setting_btn)

    def find_address(self):
        return self.find_element_by_up_swipe_page(self.address)


class MineHandle(BaseHandle):
    """
    我的页面-操作层
    """

    def __init__(self):
        self.mine_page = MinePage()

    def click_login_btn(self):
        self.mine_page.find_login_btn().click()

    def click_setting_btn(self):
        self.mine_page.find_setting_btn().click()

    def get_nickname(self):
        return self.mine_page.find_login_btn().text

    def click_address(self):
        self.mine_page.find_address().click()


class MineProxy:
    """
    我的页面-业务层
    """

    def __init__(self):
        self.mine_handle = MineHandle()

    def to_login_page(self):
        self.mine_handle.click_login_btn()

    def to_setting_page(self):
        self.mine_handle.click_setting_btn()

    def is_login(self):
        try:
            nickname = self.mine_handle.get_nickname()
            return nickname != "登录/注册"
        except:
            return False

    def to_address_page(self):
        self.mine_handle.click_address()
