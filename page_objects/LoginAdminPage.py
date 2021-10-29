from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LoginAdminPage(BasePage):
    # страница логина
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")

class LoginPage:
    CART_TOTAL = (By.ID, "cart-total")
    DESKTOPS = (By.LINK_TEXT, "Desktops")
    ACCOUNT_LOGIN = (By.ID, "account-login")
    COLUMN_RIGHT = (By.ID, "column-right")
    SEARCH = (By.ID, "search")

class Dashboard:
    BUTTON_SETTING = (By.ID, "button-setting")
    OPEN_CART = (By.LINK_TEXT, "OpenCart")
    VMAP = (By.ID, "vmap")
    NAVIGATION = (By.ID, "navigation")

class Catalog:
    CATEGORIES = (By.LINK_TEXT, "Categories")
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    FORM_CATEGORY = (By.ID, "form-category")
    BUTTON_DELETE = (By.CSS_SELECTOR, "button[type='button']")
    PAGINATION = (By.CSS_SELECTOR, "ul[class='pagination']")

class Product:
    EDIT = (By.CSS_SELECTOR, "a[data-original-title='Edit']")
    PRODUCTS = (By.LINK_TEXT, "Products")
    TAB_DATA = (By.ID, "tab-data")
    BUTTON_SAVE = (By.CSS_SELECTOR, "button[type='submit']")
    CANCEL = (By.CSS_SELECTOR, "a[data-original-title='Cancel']")
