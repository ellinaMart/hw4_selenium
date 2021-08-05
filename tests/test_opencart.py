
from selenium.webdriver.common.by import By
from page_objects.LoginAdminPage import LoginAdminPage


def test_admin_login_page(browser, base_url):
    browser.get(base_url + "/admin")
    browser.find_element(By.ID, "input-username")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")

def test_dashboard(browser, url_token):
    browser.get(url_token[0])
    browser.find_element(By.ID, "button-setting")
    browser.find_element(By.LINK_TEXT, "OpenCart")
    browser.find_element(By.ID, "vmap")
    browser.find_element(By.ID, "navigation")

def test_catalog(browser, base_url, url_token):
    categories_url = base_url + "/admin/index.php?route=catalog/category&" + url_token[1]
    browser.get(categories_url)
    browser.find_element(By.LINK_TEXT, "Categories")
    browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    browser.find_element(By.ID, "form-category")
    browser.find_element(By.CSS_SELECTOR, "button[type='button']")
    browser.find_element(By.CSS_SELECTOR, "ul[class='pagination']")

def test_product(browser, base_url, url_token):
    product_url = base_url + "/admin/index.php?route=catalog/product&" + url_token[1]
    browser.get(product_url)
    browser.find_element(By.CSS_SELECTOR, "a[data-original-title='Edit']").click()
    browser.find_element(By.LINK_TEXT, "Products")
    browser.find_element(By.ID, "tab-data")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.CSS_SELECTOR, "a[data-original-title='Cancel']")

def test_login_page(browser, base_url):
    browser.get(base_url + "/index.php?route=account/login")
    browser.find_element(By.ID, "cart-total")
    browser.find_element(By.LINK_TEXT, "Desktops")
    browser.find_element(By.ID, "account-login")
    browser.find_element(By.ID, "column-right")
    browser.find_element(By.ID, "search")

