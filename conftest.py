import pytest
import os
import logging

from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions


DRIVERS = os.path.expanduser("~/Develop/drivers")
logging.basicConfig(level=logging.INFO, filename="logs/selenium.log")


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
    url = request.config.getoption("--url")
    tolerance = request.config.getoption("--tolerance")
    headless = request.config.getoption("--headless")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    logger.info("===> Test {} started".format(test_name))

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

    #request.addfinalizer(driver.quit)

    logger.info("Browser {} started with {}".format(browser, driver.desired_capabilities))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished".format(test_name))

    def open(path=""):
        logger.info("Opening url: {}".format(url))
        return driver.get(url + path)

    driver.maximize_window()

    driver.open = open
    driver.open()
    driver.t = tolerance

    request.addfinalizer(fin)

    return driver


@pytest.fixture(scope="session", autouse=True)
def get_environment(pytestconfig):
    props = {
        'Shell': os.getenv('SHELL'),
        'Terminal': os.getenv('TERM'),
        'Stand': 'Production'
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/allure-results/environment.properties', 'w') as f:
        for k, v in props.items():
            f.write(f'{k}={v}\n')
