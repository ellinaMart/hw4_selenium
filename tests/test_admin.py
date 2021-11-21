import time
import pytest
import allure

from page_objects.AdminPage import AdminPage
from tests.data import test_admin


@allure.title("Test add product with admin role")
def test_admin_add_product(browser):
    browser.open("/admin")
    #pytest.skip('for a reason!')
    AdminPage(browser) \
        .login_user(login=test_admin['login'], password=test_admin['password']) \
        .go_to_products() \
        .add_product_button() \
        .fill_product_form(name="test_product", title="product_title", model="product_model")


@allure.title("Test delete product with admin role")
def test_admin_delete_product(browser):
    browser.open("/admin")
    AdminPage(browser) \
        .login_user(login=test_admin['login'], password=test_admin['password']) \
        .go_to_products() \
        .delete_product()

