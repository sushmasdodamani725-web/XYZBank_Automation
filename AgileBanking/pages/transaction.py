# # from selenium.webdriver.common.by import By
# #
# # class CustomerTransactionPage:
# #     def __init__(self, driver):
# #         self.driver = driver
# #
# #     def customer_login(self, customer_name):
# #         """Login as a customer using dropdown"""
# #         self.driver.find_element(By.CSS_SELECTOR, "button[ng-click='customer()']").click()
# #         customer_dropdown = self.driver.find_element(By.ID, "userSelect")
# #         for option in customer_dropdown.find_elements(By.TAG_NAME, "option"):
# #             if option.text == customer_name:
# #                 option.click()
# #                 break
# #         self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# #
# #     def deposit(self, amount):
# #         self.driver.find_element(By.CSS_SELECTOR, "button[ng-click='deposit()']").click()
# #         self.driver.find_element(By.CSS_SELECTOR, "input[ng-model='amount']").send_keys(str(amount))
# #         self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# #
# #     def withdraw(self, amount):
# #         self.driver.find_element(By.CSS_SELECTOR, "button[ng-click='withdrawl()']").click()
# #         self.driver.find_element(By.CSS_SELECTOR, "input[ng-model='amount']").send_keys(str(amount))
# #         self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# #
# #     def get_balance(self):
# #         return self.driver.find_element(By.CSS_SELECTOR, "span[ng-model='amount']").text
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

class CustomerTransactionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators
    CUSTOMER_LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Customer Login')]")
    CUSTOMER_DROPDOWN = (By.ID, "userSelect")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Login')]")
    DEPOSIT_TAB = (By.XPATH, "//button[contains(text(),'Deposit')]")
    DEPOSIT_INPUT = (By.XPATH, "//input[@ng-model='amount']")
    DEPOSIT_SUBMIT = (By.XPATH, "//button[@type='submit']")
    TRANSACTIONS_TAB = (By.XPATH, "//button[contains(text(),'Transactions')]")
    RESET_BTN = (By.XPATH, "//button[contains(text(),'Reset')]")
    LOGOUT_BTN = (By.XPATH, "//button[contains(text(),'Logout')]")

    def login_as_customer(self, customer_name):
        """Login as a specific customer"""
        self.wait.until(EC.element_to_be_clickable(self.CUSTOMER_LOGIN_BTN)).click()
        dropdown = self.wait.until(EC.presence_of_element_located(self.CUSTOMER_DROPDOWN))
        dropdown.click()
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//option[contains(text(),'{customer_name}')]"))).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

    def perform_deposit(self, amount):
        """Deposit amount and handle stale element"""
        for _ in range(3):  # retry up to 3 times if stale element
            try:
                self.wait.until(EC.element_to_be_clickable(self.DEPOSIT_TAB)).click()
                self.wait.until(EC.presence_of_element_located(self.DEPOSIT_INPUT)).send_keys(str(amount))
                self.wait.until(EC.element_to_be_clickable(self.DEPOSIT_SUBMIT)).click()
                time.sleep(2)
                break
            except StaleElementReferenceException:
                print("Retrying due to stale element during deposit...")
                time.sleep(2)

    def open_transactions(self):
        """Navigate to transactions tab"""
        for _ in range(3):
            try:
                self.wait.until(EC.element_to_be_clickable(self.TRANSACTIONS_TAB)).click()
                break
            except StaleElementReferenceException:
                print("Retrying due to stale element on Transactions tab...")
                time.sleep(2)

    def reset_transactions(self):
        """Click reset in transactions tab"""
        self.open_transactions()
        try:
            self.wait.until(EC.element_to_be_clickable(self.RESET_BTN)).click()
        except Exception:
            print("Reset button not found, skipping.")

    def logout(self):
        """Logout the customer"""
        for _ in range(3):
            try:
                self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()
                break
            except StaleElementReferenceException:
                print("Retrying logout due to stale element...")
                time.sleep(2)

