#from page_objects.MainPage import MainPage
#from page_objects.UserPage import UserPage
from page_objects.AdminPage import AdminPage
# from page_objects.ProductPage import ProductPage
# from page_objects.ComparisonPage import ComparisonPage
# from page_objects.CartPage import CartPage
#from page_objects.elements.SuccessAlert import SuccessAlert


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



#
#
#     product_name = MainPage(browser).get_featured_product_name(1)
#     MainPage(browser) \
#         .click_featured_product(1) \
#         .add_to_wishlist() \
#         .alert.click_login()
#     UserPage(browser) \
#         .login_user(email="test2@mail.ru", password="test") \
#         .open_wishlist() \
#         .verify_product(product_name)

# def test_add_to_wish_list(browser):
#     product_name = MainPage(browser).click_featured_product(1)
#     import pdb; pdb.set_trace()
#     ProductPage(browser).add_to_wish_list()
#     SuccessAlert(browser).click_login()
#     UserPage(browser) \
#         .login_with("test2@mail.ru", "test") \
#         .click_link('Wish List') \
#         .verify_product_link(product_name)
#
#
# def test_add_to_cart(browser):
#     product_name = MainPage(browser).click_featured_product(1)
#     ProductPage(browser).add_to_cart()
#     SuccessAlert(browser).click_shopping_cart()
#     CartPage(browser) \
#         .verify_product(product_name) \
#         .go_to_checkout()
#     UserPage(browser) \
#         .login_with("test2@mail.ru", "test") \
#         .verify_pay_form()
#
#
# def test_add_to_cart_from_comparison(browser):
#     product_name = MainPage(browser).click_featured_product(1)
#     ProductPage(browser).add_to_comparison()
#     SuccessAlert(browser).click_product_comparison()
#     ComparisonPage(browser) \
#         .verify_product_link(product_name) \
#         .add_to_cart()
#     SuccessAlert(browser).click_shopping_cart()
#     CartPage(browser) \
#         .verify_product(product_name) \
#         .go_to_checkout()
#     UserPage(browser) \
#         .login_with("test2@mail.ru", "test") \
#         .verify_pay_form()