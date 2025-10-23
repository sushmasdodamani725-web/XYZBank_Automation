# # # import pytest
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options
# # # from webdriver_manager.chrome import ChromeDriverManager
# # #
# # # @pytest.fixture(scope="session")
# # # def driver():
# # #     options = Options()
# # #     options.add_argument("--start-maximized")
# # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# # #     yield driver
# # #     driver.quit()
# # #
# # # @pytest.fixture(scope="session")
# # # def base_url():
# # #     return "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
# # import pytest
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # from selenium.webdriver.edge.service import Service as EdgeService
# # from selenium.webdriver.chrome.options import Options as ChromeOptions
# # from selenium.webdriver.edge.options import Options as EdgeOptions
# # from webdriver_manager.chrome import ChromeDriverManager
# # from webdriver_manager.microsoft import EdgeChromiumDriverManager
# #
# #
# # def pytest_addoption(parser):
# #     parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or edge")
# #
# #
# # @pytest.fixture(scope="session")
# # def driver(request):
# #     browser = request.config.getoption("--browser")
# #
# #     if browser.lower() == "chrome":
# #         options = ChromeOptions()
# #         options.add_argument("--start-maximized")
# #         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# #
# #     elif browser.lower() == "edge":
# #         options = EdgeOptions()
# #         options.add_argument("--start-maximized")
# #         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
# #
# #     else:
# #         raise ValueError(f"Unsupported browser: {browser}")
# #
# #     yield driver
# #     driver.quit()
# #
# #
# # @pytest.fixture(scope="session")
# # def base_url():
# #     return "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
# import pytest
# from utils.browser_setup import Browser
#
# BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
#
#
# # ✅ This will run tests for all 3 browsers automatically
# def pytest_generate_tests(metafunc):
#     if "browser_name" in metafunc.fixturenames:
#         metafunc.parametrize("browser_name", ["chrome", "firefox", "edge"])
#
#
# @pytest.fixture(scope="session")
# def driver(browser_name):
#     """Creates a WebDriver instance for each browser (Chrome, Firefox, Edge)."""
#     browser = Browser(browser_name)
#     driver = browser.get_driver()
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture(scope="session")
# def base_url():
#     return BASE_URL


# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
#from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# ✅ List of browsers to run sequentially
@pytest.fixture(params=["chrome","firefox"], scope="function")
def browser_name(request):
    return request.param


@pytest.fixture(scope="function")
def driver(browser_name):
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser_name == "firefox":
         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    # elif browser_name == "edge":
    #     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

