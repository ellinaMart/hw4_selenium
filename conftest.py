import pytest
import os
import logging

from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions


DRIVERS = os.path.expanduser("~/Develop/drivers")
logging.basicConfig(level=logging.INFO, filename="logs/selenium.log")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--bversion", action="store", default="92.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--url", "-U", default="http://demo.opencart.com/")
    parser.addoption("--tolerance", type=int, default=3)
    parser.addoption("--headless", action="store_true", help="Run headless")


@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """

    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")
    url = request.config.getoption("--url")
    tolerance = request.config.getoption("--tolerance")
    headless = request.config.getoption("--headless")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    logger.info("===> Test {} started".format(test_name))


    if executor == "local":
        caps = {'goog:chromeOptions': {}}

        if mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

        wd = webdriver.Chrome(desired_capabilities=caps)

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "screenResolution": "1280x1024",
            "name": "agr tests",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
            # 'goog:chromeOptions': {}
        }

        if browser == "chrome" and mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

        wd = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

        if not mobile:
            wd.maximize_window()

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
