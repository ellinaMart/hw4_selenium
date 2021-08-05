import pytest
import os

from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from page_objects.LoginAdminPage import LoginAdminPage


DRIVERS = os.path.expanduser("~/Develop/drivers")

def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")
    parser.addoption(
        "--url",
        action="store",
        default="https://demo.opencart.com",
        help="This is opencart url"
    )

@pytest.fixture(scope="session")
def url_token(browser, base_url):
    browser.get(base_url + "/admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).clear()
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("demo")
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).clear()
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("demo")
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()
    url_with_token = browser.current_url
    token = url_with_token.split('&')[1]
    return url_with_token, token

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="session")
def admin_url(request):
    return request.config.getoption("--admin_url")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless

        driver = webdriver.Chrome(
            options=options,
            executable_path=f"{DRIVERS}/chromedriver"
        )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = headless

        driver = webdriver.Firefox(
            options=options,
            executable_path=f"{DRIVERS}/geckodriver"
        )
    elif browser == "opera":
        options = OperaOptions()

        driver = webdriver.Opera(
            options=options,
            executable_path=f"{DRIVERS}/operadriver"
        )
    else:
        raise ValueError("Driver not supported: {}".format(browser))

    request.addfinalizer(driver.quit)

    if maximized:
        driver.maximize_window()

    return driver
