from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    ADD_CUSTOMER_BTN = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    # Methods
    def click_add_customer(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_CUSTOMER_BTN))
        btn.click()

    def fill_customer_form(self, first_name, last_name, post_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POST_CODE_INPUT).send_keys(post_code)

    def submit_customer(self):
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def add_customer(self, first_name, last_name, post_code):
        self.click_add_customer()
        self.fill_customer_form(first_name, last_name, post_code)
        self.submit_customer()
