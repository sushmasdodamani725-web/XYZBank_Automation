import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

@pytest.mark.login
def test_bank_manager_login(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)

    # Click Bank Manager Login
    login.click_bank_manager_login()

    # Wait for Add Customer button (unique to Bank Manager)
    manager_dashboard_header = (By.XPATH, "//button[contains(text(),'Add Customer')]")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(manager_dashboard_header)
    )

    # Assert dashboard is displayed
    assert driver.find_element(*manager_dashboard_header).is_displayed(), "Bank Manager dashboard not loaded"
    print("✅ Bank Manager login successful")

@pytest.mark.login
def test_customer_login(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)

    # Click Customer Login
    login.click_customer_login()

    # Select user and login
    login.select_user("Harry Potter")
    login.click_login()

    # Wait for Logout button (unique to Customer dashboard)
    logout_btn = (By.CSS_SELECTOR, "button[ng-click='byebye()']")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(logout_btn)
    )

    assert driver.find_element(*logout_btn).is_displayed(), "Customer dashboard not loaded"
    print("✅ Customer login successful")
