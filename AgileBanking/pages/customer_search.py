from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.customers_tab = (By.XPATH, "//button[contains(text(),'Customers')]")
        self.search_input = (By.XPATH, "//input[@placeholder='Search Customer']")
        self.customer_rows = (By.XPATH, "//table/tbody/tr")

    def open_customers_tab(self):
        """Click on the Customers tab"""
        self.wait.until(EC.element_to_be_clickable(self.customers_tab)).click()

    def search_customer(self, customer_name):
        """Enter customer name in the search field"""
        search_box = self.wait.until(EC.visibility_of_element_located(self.search_input))
        search_box.clear()
        search_box.send_keys(customer_name)

    def get_displayed_customers(self):
        """Return the list of displayed customer names after search"""
        self.wait.until(EC.presence_of_all_elements_located(self.customer_rows))
        rows = self.driver.find_elements(*self.customer_rows)
        return [row.text for row in rows]
