from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    BANK_MANAGER_BTN = (By.CSS_SELECTOR, "button[ng-click='manager()']")
    CUSTOMER_BTN = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[ng-click='byebye()']")
    USER_SELECT = (By.ID, "userSelect")
    ACCOUNT_SELECT = (By.ID, "accountSelect")

    # Methods
    def open(self, url):
        self.driver.get(url)

    def click_bank_manager_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.BANK_MANAGER_BTN))
        btn.click()

    def click_customer_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.CUSTOMER_BTN))
        btn.click()

    def select_user(self, username):
        user_dropdown = self.wait.until(EC.visibility_of_element_located(self.USER_SELECT))
        from selenium.webdriver.support.ui import Select
        select = Select(user_dropdown)
        select.select_by_visible_text(username)

    def select_account(self, account):
        account_dropdown = self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_SELECT))
        from selenium.webdriver.support.ui import Select
        select = Select(account_dropdown)
        select.select_by_visible_text(account)

    def click_login(self):
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN))
        login_btn.click()
