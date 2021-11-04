from page_objects.AdminPage import AdminPage


def test_admin_page(browser):
    browser.open("/admin")
    AdminPage(browser) \
        .check_elements_login_page() \
        .login_user(login="test2@mail.ru", password="test") \
        .check_elements_dashboard() \
        .go_to_categories() \
        .check_elements_categories() \
        .go_to_products() \
        .check_elements_products()
