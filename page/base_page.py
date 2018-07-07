from common.utils import DriverUtil


class BasePage(object):
    """
    基础-对象库层
    """

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element(self, location):
        print("location=", location)
        return self.driver.find_element(location[0], location[1])

    def find_element_by_up_swipe_page(self, location):
        print("find_element_by_up_swipe_page location=", location)
        while True:
            try:
                element = self.find_element(location)
                return element
            except Exception:
                print("not find element in current screen!")
                self.swipe_up()

    def find_element_by_id(self, id_value):
        return self.driver.find_element_by_id(id_value)

    def swipe_up(self):
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]
        self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 3000)


class BaseHandle(object):
    """
    基础-操作层
    """

    def send_keys(self, element, text):
        """
        在文本框中输入内容，输入前先清空
        :param element: 文本框元素
        :param text: 输入内容
        """
        element.clear()
        element.send_keys(text)
