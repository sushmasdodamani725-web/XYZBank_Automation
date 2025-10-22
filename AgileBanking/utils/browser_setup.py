# utils/browser_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

class Browser:
    def __init__(self, browser_name="chrome"):
        self.browser_name = browser_name.lower()

    def get_driver(self):
        if self.browser_name == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-popup-blocking")
            service = Service()
            driver = webdriver.Chrome(service=service, options=chrome_options)
        elif self.browser_name == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")
        driver.implicitly_wait(10)
        return driver
