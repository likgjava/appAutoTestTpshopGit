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
        # 编辑按钮
        self.edit_address_btn = (By.XPATH, "//*[@text='{}']/../android.widget.ImageView")
        # 删除按钮
        self.del_address_btn = (By.XPATH, "//*[@text='删除']")
        # 删除确定按钮
        self.del_confirm_btn = (By.ID, "com.tpshop.malls:id/positiveButton")

    def find_add_address_btn(self):
        return self.find_element(self.add_address_btn)

    def find_edit_address_btn(self, address):
        location = (self.edit_address_btn[0], self.edit_address_btn[1].format(address))
        return self.find_element(location)

    def find_del_address_btn(self):
        return self.find_element(self.del_address_btn)

    def find_del_confirm_btn(self):
        return self.find_element(self.del_confirm_btn)


class AddressHandle(BaseHandle):
    """
    收货地址页面-操作层
    """

    def __init__(self):
        self.address_page = AddressPage()

    def click_add_address_btn(self):
        self.address_page.find_add_address_btn().click()

    def click_edit_address_btn(self, address):
        self.address_page.find_edit_address_btn(address).click()

    def click_del_address_btn(self):
        self.address_page.find_del_address_btn().click()

    def click_del_confirm_btn(self):
        self.address_page.find_del_confirm_btn().click()


class AddressProxy:
    """
    收货地址页面-业务层
    """

    def __init__(self):
        self.address_handle = AddressHandle()

    def to_add_address_page(self):
        self.address_handle.click_add_address_btn()

    def del_address(self, address):
        self.address_handle.click_edit_address_btn(address)
        self.address_handle.click_del_address_btn()
        self.address_handle.click_del_confirm_btn()

