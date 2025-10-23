# # utils/browser_setup.py
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import pytest
#
# class Browser:
#     def __init__(self, browser_name="chrome"):
#         self.browser_name = browser_name.lower()
#
#     def get_driver(self):
#         if self.browser_name == "chrome":
#             chrome_options = Options()
#             chrome_options.add_argument("--start-maximized")
#             chrome_options.add_argument("--disable-notifications")
#             chrome_options.add_argument("--disable-popup-blocking")
#             service = Service()
#             driver = webdriver.Chrome(service=service, options=chrome_options)
#         elif self.browser_name == "firefox":
#             driver = webdriver.Firefox()
#         else:
#             raise ValueError(f"Unsupported browser: {self.browser_name}")
#         driver.implicitly_wait(10)
#         return driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Browser:
    def __init__(self, browser_name="chrome"):
        self.browser_name = browser_name.lower()

    def get_driver(self):
        if self.browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        elif self.browser_name == "edge":
            options = EdgeOptions()
            options.add_argument("--start-maximized")
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)

        elif self.browser_name == "firefox":
            options = FirefoxOptions()
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

        driver.implicitly_wait(10)
        return driver
