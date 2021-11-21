import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    USERNAME_INPUT = {'css': '#input-username'}
    PASSWORD_INPUT = {'css': '#input-password'}
    SUBMIT_BUTTON = {'css': 'button[type=submit]'}
    CATALOG_BUTTON = {'css': '#menu-catalog'}
    ADD_NEW = {'css': 'a[data-original-title="Add New"]'}
    PRODUCTS_BUTTON = {'xpath': "//*[text()='Products']"}
    CATEGORIES_BUTTON = {'xpath': "//*[text()='Categories']"}
    PRODUCT_NAME = {'css': '#input-name1'}
    PRODUCT_TITLE = {'css': '#input-meta-title1'}
    DATA = {'xpath': "//*[text()='Data']"}
    PRODUCT_MODEL = {'css': '#input-model'}
    PRODUCT_CHECKBOX = {'css': '*[type=checkbox]'}
    DELETE_BUTTON = {'css': 'i[class="fa fa-trash-o"]'}
    OPENCART_LINK = {'xpath': "//*[text()='OpenCart']"}
    FORGOTTEN_PASSWORD = {'xpath': "//*[text()='Forgotten Password']"}
    BUTTON_SETTING = {'css': '#button-setting'}
    OPEN_CART = {'xpath':  "//*[text()='OpenCart']"}
    VMAP = {'css': '#vmap'}
    NAVIGATION = {'css': '#navigation'}
    SORT_ORDER = {'xpath': "//*[text()='Sort Order']"}
    CHECKBOX = {'css': 'input[type=checkbox]'}
    FORM_CATEGORY = {'css': '#form-category'}
    BUTTON_DELETE = {'css': 'button[type=button]'}
    PAGINATION = {'css': 'ul[class="pagination"]'}
    EDIT = {'css': 'a[data-original-title=Edit]'}
    COPY = {'css': 'button[data-original-title=Copy]'}
    DELETE = {'css': 'button[data-original-title=Delete]'}
    FILTER = {'css': '#filter-product'}

    @allure.step("Login with user role {login}, {password}")
    def login_user(self, login, password):
        self._input(self.USERNAME_INPUT, login)
        self._input(self.PASSWORD_INPUT, password)
        self._click(self.SUBMIT_BUTTON)
        return self

    @allure.step("Go to products page")
    def go_to_products(self):
        self._click(self.CATALOG_BUTTON)
        self._click(self.PRODUCTS_BUTTON)
        return self

    @allure.step("Go to categories page")
    def go_to_categories(self):
        self._click(self.CATALOG_BUTTON)
        self._click(self.CATEGORIES_BUTTON)
        return self

    @allure.step("Add product")
    def add_product_button(self):
        self._click(self.ADD_NEW)
        return self

    @allure.step("Fill product page")
    def fill_product_form(self, name, title, model):
        self._input(self.PRODUCT_NAME, name)
        self._input(self.PRODUCT_TITLE, title)
        self._click(self.DATA)
        self._input(self.PRODUCT_MODEL, model)
        self._click(self.SUBMIT_BUTTON)
        return self

    @allure.step("Delete product")
    def delete_product(self):
        self._click(self.PRODUCT_CHECKBOX, index=1)
        self._wait_for_visible(self.DELETE_BUTTON)
        self._click(self.DELETE_BUTTON)
        return self

    @allure.step("Check elements on admin login page")
    def check_elements_login_page(self):
        self._wait_for_visible(self.USERNAME_INPUT)
        self._wait_for_visible(self.PASSWORD_INPUT)
        self._wait_for_visible(self.SUBMIT_BUTTON)
        self._wait_for_visible(self.OPENCART_LINK)
        self._wait_for_visible(self.FORGOTTEN_PASSWORD)
        return self

    @allure.step("Check elements on dashboard")
    def check_elements_dashboard(self):
        self._wait_for_visible(self.BUTTON_SETTING)
        self._wait_for_visible(self.OPEN_CART)
        self._wait_for_visible(self.VMAP)
        self._wait_for_visible(self.NAVIGATION)
        return self

    @allure.step("Check elements onn categories page")
    def check_elements_categories(self):
        self._wait_for_visible(self.SORT_ORDER)
        self._wait_for_visible(self.CHECKBOX)
        self._wait_for_visible(self.FORM_CATEGORY)
        self._wait_for_visible(self.BUTTON_DELETE)
        self._wait_for_visible(self.PAGINATION)
        return self

    @allure.step("Check elements on products page")
    def check_elements_products(self):
        self._wait_for_visible(self.EDIT)
        self._wait_for_visible(self.ADD_NEW)
        self._wait_for_visible(self.COPY)
        self._wait_for_visible(self.DELETE)
        self._wait_for_visible(self.FILTER)
        return self

