import pytest
import os

from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions


DRIVERS = os.path.expanduser("~/Develop/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", default="chrome")
    #parser.addoption("--executor", "-E", default="127.0.0.1")
    parser.addoption("--url", "-U", default="http://demo.opencart.com/")
    parser.addoption("--tolerance", type=int, default=3)
    parser.addoption("--headless", action="store_true", help="Run headless")


@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """

    browser = request.config.getoption("--browser")
    #executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    tolerance = request.config.getoption("--tolerance")
    headless = request.config.getoption("--headless")

    # https://www.selenium.dev/documentation/en/webdriver/page_loading_strategy/
    common_caps = {"pageLoadStrategy": "eager"}
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless

        driver = webdriver.Chrome(
            options=options,
            executable_path=f"{DRIVERS}/chromedriver 2"
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
    # if executor == "local":
    #     driver = webdriver.Chrome(
    #         executable_path=f"{DRIVERS}/chromedriver",
    #         desired_capabilities=common_caps
    #     )
    # else:
    #
    #     desired_capabilities = {
    #         "browser": browser,
    #         **common_caps
    #     }

        # driver = webdriver.Remote(
        #     desired_capabilities=desired_capabilities,
        #     command_executor=f"http://{executor}:4444/wd/hub",
        # )

    request.addfinalizer(driver.quit)

    def open(path=""):
        return driver.get(url + path)

    driver.maximize_window()

    driver.open = open
    driver.open()
    driver.t = tolerance

    return driver
