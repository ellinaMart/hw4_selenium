#from page_objects.AdminPage import *
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






#
# def test_admin_login_page(browser, ):
#     browser.open("/admin")
#
#     browser.find_element(*LoginAdminPage.USERNAME_INPUT)
#     browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
#     browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
#     browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
#     browser.find_element(*LoginAdminPage.OPENCART_LINK)

# def test_dashboard(browser, url_token):
#     browser.get(url_token[0])
#     browser.find_element(*Dashboard.BUTTON_SETTING)
#     browser.find_element(*Dashboard.OPEN_CART)
#     browser.find_element(*Dashboard.VMAP)
#     browser.find_element(*Dashboard.NAVIGATION)

# def test_catalog(browser, base_url, url_token):
#     categories_url = base_url + "/admin/index.php?route=catalog/category&" + url_token[1]
#     browser.get(categories_url)
#     browser.find_element(*Catalog.CATEGORIES)
#     browser.find_element(*Catalog.CHECKBOX)
#     browser.find_element(*Catalog.FORM_CATEGORY)
#     browser.find_element(*Catalog.BUTTON_DELETE)
#     browser.find_element(*Catalog.PAGINATION)
#
# def test_product(browser, base_url, url_token):
#     product_url = base_url + "/admin/index.php?route=catalog/product&" + url_token[1]
#     browser.get(product_url)
#     browser.find_element(*Product.EDIT).click()
#     browser.find_element(*Product.PRODUCTS)
#     browser.find_element(*Product.TAB_DATA)
#     browser.find_element(*Product.BUTTON_SAVE)
#     browser.find_element(*Product.CANCEL)
#
# def test_login_page(browser, base_url):
#     browser.get(base_url + "/index.php?route=account/login")
#     browser.find_element(*LoginPage.CART_TOTAL)
#     browser.find_element(*LoginPage.DESKTOPS)
#     browser.find_element(*LoginPage.ACCOUNT_LOGIN)
#     browser.find_element(*LoginPage.COLUMN_RIGHT)
#     browser.find_element(*LoginPage.SEARCH)
