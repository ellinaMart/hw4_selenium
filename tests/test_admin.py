from page_objects.AdminPage import AdminPage


def test_admin_add_product(browser):
    browser.open("/admin")
    AdminPage(browser) \
        .login_user(login="test2@mail.ru", password="test") \
        .go_to_products() \
        .add_product_button() \
        .fill_product_form(name="test_product", title="product_title", model="product_model")

def test_admin_delete_product(browser):
    browser.open("/admin")
    AdminPage(browser) \
        .login_user(login="test2@mail.ru", password="test") \
        .go_to_products() \
        .delete_product()
