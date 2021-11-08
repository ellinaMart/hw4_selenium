import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .common.Alert import Alert
import logging


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.alert = Alert(self.driver)
        self.logger = logging.getLogger(type(self).__name__)


    def __element(self, selector: dict, index: int, link_text: str = None):
        self.logger.info("Find element {}".format(selector))
        by = None
        if link_text:
            by = By.LINK_TEXT
        if 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)[index]

    def _click_link(self, link_text):
        return self.driver.find_element(By.LINK_TEXT, link_text)

    def _click(self, selector, index=0):
        self.logger.info("Clicking element: {}".format(selector))
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        self.logger.info("Input {} in input {}".format(value, selector))
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=20):
        self.logger.info("Check if element {} is present".format(selector))
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index, link_text)))

    def _get_element_text(self, selector, index):
        self.logger.info("Get element {} text".format(selector))
        return self.__element(selector, index).text

