from page_objects.AdminPage import AdminPage
from tests.data import test_admin


def test_admin_page(browser):
    browser.open("/admin")
    AdminPage(browser) \
        .check_elements_login_page() \
        .login_user(login=test_admin['login'], password=test_admin['password']) \
        .check_elements_dashboard() \
        .go_to_categories() \
        .check_elements_categories() \
        .go_to_products() \
        .check_elements_products()
