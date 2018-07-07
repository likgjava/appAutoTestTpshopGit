from selenium.webdriver.common.by import By

from page.base_page import BasePage, BaseHandle


class AddressPage(BasePage):
    """
    收货地址页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 新建地址
        self.add_address_btn = (By.ID, "com.tpshop.malls:id/add_address_btn")

    def find_add_address_btn(self):
        return self.find_element(self.add_address_btn)


class AddressHandle(BaseHandle):
    """
    收货地址页面-操作层
    """

    def __init__(self):
        self.address_page = AddressPage()

    def click_add_address_btn(self):
        self.address_page.find_add_address_btn().click()


class AddressProxy:
    """
    收货地址页面-业务层
    """

    def __init__(self):
        self.address_handle = AddressHandle()

    def to_add_address_page(self):
        self.address_handle.click_add_address_btn()

