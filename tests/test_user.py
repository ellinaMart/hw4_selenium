import random
from page_objects.UserPage import UserPage


def test_user_register(browser):
    browser.open()
    UserPage(browser) \
        .open_register_form() \
        .fill_register_form(firstname="Ivan", lastname="Ivanov", email="ivan+%s@test.ru"%random.randint(0,20), phone="+79271234567", password="Ivan12") \
        .check_account_created()

def test_change_currency(browser):
    browser.open()
    UserPage(browser) \
        .open_login_form() \
        .login_user(email="ivan@test.ru", password="Ivan12") \
        .change_currency()

