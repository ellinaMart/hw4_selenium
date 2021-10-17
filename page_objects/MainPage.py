# from selenium.webdriver.common.by import By
#
# from .BasePage import BasePage
#
#
# class MainPage(BasePage):
#     FEATURE_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
#     FEATURE_PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")
#
#     def click_featured_product(self, number):
#         index = number - 1
#         feature_product = self.browser.find_elements(*self.FEATURE_PRODUCT)[index]
#         product_name = feature_product.find_element(*self.FEATURE_PRODUCT_NAME).text
#         feature_product.click()
#         return product_name

from .BasePage import BasePage
from .ProductPage import ProductPage


class MainPage(BasePage):
    """Главная страница"""

    IT = {'css': '#content > div.row'}
    PRODUCTS = {'css': IT['css'] + ' .product-layout'}
    PRODUCT_NAMES = {'css': PRODUCTS['css'] + ' .caption h4 a'}

    def click_featured_product(self, number):
        index = number - 1
        self._click(self.PRODUCTS, index=index)
        return ProductPage(self.driver)

    def get_featured_product_name(self, number):
        index = number - 1
        #import pdb; pdb.set_trace()
        return self._get_element_text(self.PRODUCT_NAMES, index=index)