import allure

from .BasePage import BasePage


class UserPage(BasePage):
    """Страница пользователя"""
    RIGHT_MENU = {'css': '#column-right'}
    WISH_LIST = {'css': RIGHT_MENU['css'] + ' a:nth-child(5)'}
    PAYMENT_FORM = {'css': '#payment-new'}
    LOGIN_EMAIL_INPUT = {'css': '#input-email'}
    LOGIN_PASSWORD_INPUT = {'css': '#input-password'}
    LOGIN_BUTTON = {'css': 'input[value=Login]'}
    CARET_BUTTON = {'css': 'span[class="caret"]'}
    REGISTER_BUTTON = {'xpath': "//*[text()='Register']"}
    USER_FIRSTNAME = {'css': '#input-firstname'}
    USER_LASTNAME = {'css': '#input-lastname'}
    USER_EMAIL = {'css': '#input-email'}
    USER_PHONE = {'css': '#input-telephone'}
    USER_PASSWORD = {'css': '#input-password'}
    USER_CONFIRM = {'css': '#input-confirm'}
    USER_AGREE = {'css': 'input[type="checkbox"]'}
    USER_SUBMIT = {'css': 'input[type="submit"]'}
    USER_CONTENT = {'css': '#content'}
    CARET_CURRENCY = {'css': '#form-currency'}
    GBP_BUTTON = {'css': 'button[name="GBP"]'}
    LOGIN_BUTTON_1 = {'xpath': "//*[text()='Login']"}

    @allure.step("Open user register form")
    def open_register_form(self):
        self._click(self.CARET_BUTTON)
        self._click(self.REGISTER_BUTTON)
        return self

    @allure.step("Fill user register form with {email}, {password}")
    def fill_register_form(self, firstname, lastname, email, phone, password):
        self._input(self.USER_FIRSTNAME, firstname)
        self._input(self.USER_LASTNAME, lastname)
        self._input(self.USER_EMAIL, email)
        self._input(self.USER_PHONE, phone)
        self._input(self.USER_PASSWORD, password)
        self._input(self.USER_CONFIRM, password)
        self._click(self.USER_AGREE)
        self._click(self.USER_SUBMIT)
        return self

    @allure.step("Check user account created")
    def check_account_created(self):
        self._wait_for_visible(self.USER_CONTENT)
        return self

    @allure.step("Open user login form")
    def open_login_form(self):
        self._click(self.CARET_BUTTON)
        self._click(self.LOGIN_BUTTON_1)
        return self

    @allure.step("Login user with {email}, {password}")
    def login_user(self, email, password):
        self._input(self.LOGIN_EMAIL_INPUT, email)
        self._input(self.LOGIN_PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)
        return self

    @allure.step("Change currency with user role")
    def change_currency(self):
        self._click(self.CARET_CURRENCY)
        self._click(self.GBP_BUTTON)
        return self

    @allure.step("Open wishlist")
    def open_wishlist(self):
        self._click(self.WISH_LIST)
        return self

    @allure.step("Verify payment form")
    def verify_payment_form(self):
        self._wait_for_visible(self.PAYMENT_FORM)
        return self

    @allure.step("Verify product page")
    def verify_product(self, name):
        self._wait_for_visible(name, link_text=True)
        return self