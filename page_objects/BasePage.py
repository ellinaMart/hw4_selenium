# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class BasePage:
#
#     def __init__(self, browser):
#         self.browser = browser
#
#     def _verify_link_presence(self, link_text):
#         try:
#             return WebDriverWait(self.browser, self.browser.t) \
#                 .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
#         except TimeoutException:
#             raise AssertionError("Cant find element by link text: {}".format(link_text))
#
#     def _verify_element_presence(self, locator: tuple):
#         try:
#             return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
#         except TimeoutException:
#             raise AssertionError("Cant find element by locator: {}".format(locator))
#
#     def _element(self, locator: tuple):
#         return self._verify_element_presence(locator)
#
#     def _click_element(self, element):
#         ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()
#
#     def _simple_click_element(self, element):
#         element.click()
#
#     def _click(self, locator: tuple):
#         element = self._element(locator)
#         ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()
#
#     def _click_in_element(self, element, locator: tuple, index: int = 0):
#         element = element.find_elements(*locator)[index]
#         self._click_element(element)
#
#     def click_link(self, link_text):
#         self._click((By.LINK_TEXT, link_text))
#         return self

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .common.Alert import Alert


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.alert = Alert(self.driver)

        #self.driver.find_element_by_css_selector(self.SUCCESS_ALERT_LOGIN['css']).click()

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        #import pdb; pdb.set_trace()
        if link_text:
            by = By.LINK_TEXT
        if 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        #import pdb; pdb.set_trace()
        return self.driver.find_elements(by, selector)[index]

    def _click_link(self, link_text):
        #import pdb; pdb.set_trace()
        import time;
        time.sleep(5)
        return self.driver.find_element(By.LINK_TEXT, link_text)

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=20):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index, link_text)))

    def _get_element_text(self, selector, index):
        return self.__element(selector, index).text
