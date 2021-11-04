import random
from page_objects.UserPage import UserPage
from tests.data import test_user, new_test_user


def test_user_register(browser):
    browser.open()
    UserPage(browser) \
        .open_register_form() \
        .fill_register_form(firstname=new_test_user['name'],
                            lastname=new_test_user['lastname'],
                            email=new_test_user['login'],
                            phone=new_test_user['phone'],
                            password=new_test_user['password']) \
        .check_account_created()

def test_change_currency(browser):
    browser.open()
    UserPage(browser) \
        .open_login_form() \
        .login_user(email=test_user['login'], password=test_user['password']) \
        .change_currency()

