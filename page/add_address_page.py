from selenium.webdriver.common.by import By

from page.base_page import BasePage, BaseHandle


class AddAddressPage(BasePage):
    """
    新增收货地址页面-对象库层
    """

    def __init__(self):
        super().__init__()

        # 收货人
        self.name = (By.ID, "com.tpshop.malls:id/consignee_name_edtv")
        # 手机号码
        self.mobile = (By.ID, "com.tpshop.malls:id/consignee_mobile_edtv")
        # 所在地区
        self.region = (By.ID, "com.tpshop.malls:id/consignee_region_txtv")
        # 详细地址
        self.address = (By.ID, "com.tpshop.malls:id/consignee_address_edtv")
        # 设置默认
        self.set_default = (By.ID, "com.tpshop.malls:id/set_default_sth")
        # 保存收货地址
        self.submit_btn = (By.ID, "com.tpshop.malls:id/submit_btn")

        # 省
        self.province = [By.XPATH, "//*[@text='{}']"]
        # 市
        self.city = [By.XPATH, "//*[@text='{}']"]
        # 县
        self.district = [By.XPATH, "//*[@text='{}']"]
        # 镇
        self.town = [By.XPATH, "//*[@text='{}']"]
        # 确定按钮
        self.right_btn = (By.ID, "com.tpshop.malls:id/btn_right")

    def find_name(self):
        return self.find_element(self.name)

    def find_mobile(self):
        return self.find_element(self.mobile)

    def find_region(self):
        return self.find_element(self.region)

    def find_address(self):
        return self.find_element(self.address)

    def find_set_default(self):
        return self.find_element(self.set_default)

    def find_submit_btn(self):
        return self.find_element(self.submit_btn)

    def find_province(self, province):
        self.province[1] = self.province[1].format(province)
        return self.find_element(self.province)

    def find_city(self, city):
        self.city[1] = self.city[1].format(city)
        return self.find_element(self.city)

    def find_district(self, district):
        self.district[1] = self.district[1].format(district)
        return self.find_element(self.district)

    def find_town(self, town):
        self.town[1] = self.town[1].format(town)
        return self.find_element(self.town)

    def find_right_btn(self):
        return self.find_element(self.right_btn)


class AddAddressHandle(BaseHandle):
    """
    收货地址页面-操作层
    """

    def __init__(self):
        self.add_address_page = AddAddressPage()

    def input_name(self, name):
        self.send_keys(self.add_address_page.find_name(), name)

    def input_mobile(self, mobile):
        self.send_keys(self.add_address_page.find_mobile(), mobile)

    def click_region(self):
        self.add_address_page.find_region().click()

    def input_address(self, address):
        self.send_keys(self.add_address_page.find_address(), address)

    def click_submit_btn(self):
        self.add_address_page.find_submit_btn().click()

    def select_province(self, province):
        self.add_address_page.find_province(province).click()

    def select_city(self, city):
        self.add_address_page.find_city(city).click()

    def select_district(self, district):
        self.add_address_page.find_district(district).click()

    def select_town(self, town):
        self.add_address_page.find_town(town).click()

    def click_right_btn(self):
        self.add_address_page.find_right_btn().click()


class AddAddressProxy:
    """
    新增收货地址页面-业务层
    """

    def __init__(self):
        self.add_address_handle = AddAddressHandle()

    def add_address(self, name, mobile, province, city, district, town, address):
        self.add_address_handle.input_name(name)
        self.add_address_handle.input_mobile(mobile)
        self.add_address_handle.click_region()
        self.add_address_handle.select_province(province)
        self.add_address_handle.select_city(city)
        self.add_address_handle.select_district(district)
        self.add_address_handle.select_town(town)
        self.add_address_handle.click_right_btn()
        self.add_address_handle.input_address(address)
        self.add_address_handle.click_submit_btn()
