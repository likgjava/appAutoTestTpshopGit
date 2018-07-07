from selenium.webdriver.common.by import By

from page.base_page import BasePage, BaseHandle


class MainPage(BasePage):
    """
    主页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 我的
        self.mine_btn = (By.XPATH, "//*[@text='我的']")

    def find_mine_btn(self):
        return self.find_element(self.mine_btn)


class MainHandle(BaseHandle):
    """
    主页面-操作层
    """

    def __init__(self):
        self.main_page = MainPage()

    def click_mine_btn(self):
        self.main_page.find_mine_btn().click()


class MainProxy:
    """
    主页面-业务层
    """

    def __init__(self):
        self.main_handle = MainHandle()

    def to_mine_page(self):
        self.main_handle.click_mine_btn()
