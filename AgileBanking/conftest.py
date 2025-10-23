#
#
# # conftest.py
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# #from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
#
# # ✅ List of browsers to run sequentially
# @pytest.fixture(params=["chrome","firefox"], scope="function")
# def browser_name(request):
#     return request.param
#
#
# @pytest.fixture(scope="function")
# def driver(browser_name):
#     if browser_name == "chrome":
#         options = Options()
#         options.add_argument("--start-maximized")
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#
#     elif browser_name == "firefox":
#          driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
#     # elif browser_name == "edge":
#     #     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}")
#
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture(scope="session")
# def base_url():
#     return "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
#




# conftest.py
import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
#from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

# ✅ List of browsers to run sequentially
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser_name(request):
    return request.param


@pytest.fixture(scope="function")
def driver(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # unique temp profile
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless=new")  # headless mode for CI
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")  # headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

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
