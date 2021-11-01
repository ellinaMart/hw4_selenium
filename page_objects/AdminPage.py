from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LoginAdminPage(BasePage):
    USERNAME_INPUT = {'css': '#input-username'}
    PASSWORD_INPUT = {'css': '#input-password'}
    SUBMIT_BUTTON = {'css': 'button[type=submit]'}
    CATALOG_BUTTON = {'css': '#menu-catalog'}
    ADD_NEW = {'css': 'a[data-original-title="Add New"]'}
    PRODUCTS_BUTTON = {'xpath': "//*[text()='Products']"}
    PRODUCT_NAME = {'css': '#input-name1'}
    PRODUCT_TITLE = {'css': '#input-meta-title1'}
    DATA = {'xpath': "//*[text()='Data']"}
    PRODUCT_MODEL = {'css': '#input-model'}
    PRODUCT_CHECKBOX = {'css': '*[type=checkbox]'}
    DELETE_BUTTON = {'css': 'i[class="fa fa-trash-o"]'}


    # OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    # FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")

    def login_user(self, login, password):
        self._input(self.USERNAME_INPUT, login)
        self._input(self.PASSWORD_INPUT, password)
        self._click(self.SUBMIT_BUTTON)
        return self

    def go_to_products(self):
        self._click(self.CATALOG_BUTTON)
        import time
        time.sleep(3)
        self._click(self.PRODUCTS_BUTTON)
        return self

    def add_product_button(self):
        import time
        time.sleep(3)
        self._click(self.ADD_NEW)
        return self

    def fill_product_form(self, name, title, model):
        self._input(self.PRODUCT_NAME, name)
        self._input(self.PRODUCT_TITLE, title)
        self._click(self.DATA)
        self._input(self.PRODUCT_MODEL, model)
        self._click(self.SUBMIT_BUTTON)
        import time; time.sleep(3)
        return self

    def delete_product(self):
        self._click(self.PRODUCT_CHECKBOX, index=1)
        #import time; time.sleep(5)
        self._wait_for_visible(self.DELETE_BUTTON)
        self._click(self.DELETE_BUTTON)
        return self



class LoginPage:
    CART_TOTAL = (By.ID, "cart-total")
    DESKTOPS = (By.LINK_TEXT, "Desktops")
    ACCOUNT_LOGIN = (By.ID, "account-login")
    COLUMN_RIGHT = (By.ID, "column-right")
    SEARCH = (By.ID, "search")

class Dashboard:
    BUTTON_SETTING = (By.ID, "button-setting")
    OPEN_CART = (By.LINK_TEXT, "OpenCart")
    VMAP = (By.ID, "vmap")
    NAVIGATION = (By.ID, "navigation")

class Catalog:
    CATEGORIES = (By.LINK_TEXT, "Categories")
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    FORM_CATEGORY = (By.ID, "form-category")
    BUTTON_DELETE = (By.CSS_SELECTOR, "button[type='button']")
    PAGINATION = (By.CSS_SELECTOR, "ul[class='pagination']")

class Product:
    EDIT = (By.CSS_SELECTOR, "a[data-original-title='Edit']")
    PRODUCTS = (By.LINK_TEXT, "Products")
    TAB_DATA = (By.ID, "tab-data")
    BUTTON_SAVE = (By.CSS_SELECTOR, "button[type='submit']")
    CANCEL = (By.CSS_SELECTOR, "a[data-original-title='Cancel']")
