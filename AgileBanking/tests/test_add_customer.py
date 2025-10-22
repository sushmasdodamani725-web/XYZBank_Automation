import pytest
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

@pytest.mark.customer
def test_add_customer(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)

    # Login as Bank Manager
    login.click_bank_manager_login()

    customer_page = CustomerPage(driver)

    # Add a new customer
    first_name = "Ravi"
    last_name = "Kumar"
    post_code = "560001"
    customer_page.add_customer(first_name, last_name, post_code)

    # Handle alert popup
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"✅ Alert text: {alert_text}")
    alert.accept()

    assert "Customer added successfully" in alert_text, "Customer not added!"
