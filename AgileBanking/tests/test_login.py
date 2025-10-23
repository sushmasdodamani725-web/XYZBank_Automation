# # import pytest
# # from pages.login_page import LoginPage
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
# #
# # @pytest.mark.login
# # def test_bank_manager_login(driver):
# #     login = LoginPage(driver)
# #     login.open(BASE_URL)
# #
# #     # Click Bank Manager Login
# #     login.click_bank_manager_login()
# #
# #     # Wait for Add Customer button (unique to Bank Manager)
# #     manager_dashboard_header = (By.XPATH, "//button[contains(text(),'Add Customer')]")
# #     WebDriverWait(driver, 10).until(
# #         EC.visibility_of_element_located(manager_dashboard_header)
# #     )
# #
# #     # Assert dashboard is displayed
# #     assert driver.find_element(*manager_dashboard_header).is_displayed(), "Bank Manager dashboard not loaded"
# #     print("✅ Bank Manager login successful")
# #
# # @pytest.mark.login
# # def test_customer_login(driver):
# #     login = LoginPage(driver)
# #     login.open(BASE_URL)
# #
# #     # Click Customer Login
# #     login.click_customer_login()
# #
# #     # Select user and login
# #     login.select_user("Harry Potter")
# #     login.click_login()
# #
# #     # Wait for Logout button (unique to Customer dashboard)
# #     logout_btn = (By.CSS_SELECTOR, "button[ng-click='byebye()']")
# #     WebDriverWait(driver, 10).until(
# #         EC.visibility_of_element_located(logout_btn)
# #     )
# #
# #     assert driver.find_element(*logout_btn).is_displayed(), "Customer dashboard not loaded"
# #     print("✅ Customer login successful")
# import pytest
# from pages.login_page import LoginPage
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
#
#
# @pytest.mark.login
# def test_bank_manager_login(driver):
#     """Verify Bank Manager can log in successfully"""
#     login = LoginPage(driver)
#     login.open(BASE_URL)
#     login.click_bank_manager_login()
#
#     manager_dashboard_header = (By.XPATH, "//button[contains(text(),'Add Customer')]")
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(manager_dashboard_header))
#     assert driver.find_element(*manager_dashboard_header).is_displayed(), "Bank Manager dashboard not loaded"
#     print("✅ Bank Manager login successful")
#
#
# @pytest.mark.login
# def test_customer_login(driver):
#     """Verify Customer can log in successfully"""
#     login = LoginPage(driver)
#     login.open(BASE_URL)
#     login.click_customer_login()
#     login.select_user("Harry Potter")
#     login.click_login()
#
#     logout_btn = (By.CSS_SELECTOR, "button[ng-click='byebye()']")
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(logout_btn))
#     assert driver.find_element(*logout_btn).is_displayed(), "Customer dashboard not loaded"
#     print("✅ Customer login successful")
#
#
# @pytest.mark.login
# def test_customer_logout(driver):
#     """Verify Customer can log out successfully"""
#     login = LoginPage(driver)
#     login.open(BASE_URL)
#     login.click_customer_login()
#     login.select_user("Harry Potter")
#     login.click_login()
#
#     logout_btn = (By.CSS_SELECTOR, "button[ng-click='byebye()']")
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(logout_btn))
#     driver.find_element(*logout_btn).click()
#
#     # After logout, the login button should reappear
#     home_login_btn = (By.XPATH, "//button[contains(text(),'Customer Login')]")
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(home_login_btn))
#     assert driver.find_element(*home_login_btn).is_displayed(), "Logout failed"
#     print("✅ Customer logout successful")
#
#
# @pytest.mark.login
# def test_invalid_customer_selection(driver):
#     """Verify login does not proceed without selecting a user"""
#     login = LoginPage(driver)
#     login.open(BASE_URL)
#     login.click_customer_login()
#     login.click_login()  # Without selecting a user
#
#     # Expect same page (login page)
#     current_url = driver.current_url
#     assert "#/customer" not in current_url, "Unexpectedly navigated to customer page without selection"
#     print("✅ Customer cannot log in without selecting a name")
#
#
# @pytest.mark.login
# def test_home_button_navigation(driver):
#     """Verify Home button redirects to login page"""
#     login = LoginPage(driver)
#     login.open(BASE_URL)
#     login.click_customer_login()
#     login.select_user("Harry Potter")
#     login.click_login()
#
#     # Click Home button
#     home_btn = (By.XPATH, "//button[contains(text(),'Home')]")
#     driver.find_element(*home_btn).click()
#
#     # Verify it returned to home page
#     login_header = (By.XPATH, "//strong[contains(text(),'XYZ Bank')]")
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(login_header))
#     assert "Bank" in driver.title or driver.find_element(*login_header).is_displayed(), "Home button did not navigate back"
#     print("✅ Home button navigation successful")
#
#
# @pytest.mark.login
# def test_multiple_login_attempts(driver):
#     """Verify multiple login attempts work properly"""
#     login = LoginPage(driver)
#     login.open(BASE_URL)
#     login.click_customer_login()
#     users = ["Harry Potter", "Ron Weasly", "Hermoine Granger"]
#
#     for user in users:
#         login.select_user(user)
#         login.click_login()
#
#         logout_btn = (By.CSS_SELECTOR, "button[ng-click='byebye()']")
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(logout_btn))
#         assert driver.find_element(*logout_btn).is_displayed(), f"{user} login failed"
#         driver.find_element(*logout_btn).click()
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Customer Login')]")))
#         login.click_customer_login()
#
#     print("✅ All customer login attempts successful")

import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"


@pytest.mark.login
def test_bank_manager_login(driver):
    """Verify Bank Manager can log in successfully"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.click_bank_manager_login()

    manager_dashboard_header = (By.XPATH, "//button[contains(text(),'Add Customer')]")
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(manager_dashboard_header))
    assert driver.find_element(*manager_dashboard_header).is_displayed(), "Bank Manager dashboard not loaded"
    print("✅ Bank Manager login successful")


@pytest.mark.login
def test_customer_login(driver):
    """Verify Customer can log in successfully"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.click_customer_login()

    # Wait and select user safely
    try:
        dropdown = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "userSelect"))
        )
        dropdown.click()
        option = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='Harry Potter']"))
        )
        option.click()
    except (StaleElementReferenceException, TimeoutException):
        driver.refresh()
        dropdown = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "userSelect"))
        )
        dropdown.click()
        driver.find_element(By.XPATH, "//option[text()='Harry Potter']").click()

    login.click_login()
    logout_btn = (By.CSS_SELECTOR, "button[ng-click='byebye()']")
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(logout_btn))
    assert driver.find_element(*logout_btn).is_displayed(), "Customer dashboard not loaded"
    print("✅ Customer login successful")


@pytest.mark.login
def test_customer_logout(driver):
    """Verify Customer can log out successfully"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.click_customer_login()
    login.select_user("Harry Potter")
    login.click_login()

    logout_btn = (By.CSS_SELECTOR, "button[ng-click='byebye()']")
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(logout_btn)).click()

    home_login_btn = (By.XPATH, "//button[contains(text(),'Customer Login')]")
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(home_login_btn))
    assert driver.find_element(*home_login_btn).is_displayed(), "Logout failed"
    print("✅ Customer logout successful")


@pytest.mark.login
def test_invalid_customer_selection(driver):
    """Verify login does not proceed without selecting a user"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.click_customer_login()
    login.click_login()  # Without selecting a user

    current_url = driver.current_url
    assert "#/customer" not in current_url, "Unexpectedly navigated to customer page without selection"
    print("✅ Customer cannot log in without selecting a name")


@pytest.mark.login
def test_home_button_navigation(driver):
    """Verify Home button redirects to login page"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.click_customer_login()
    login.select_user("Harry Potter")
    login.click_login()

    home_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Home')]"))
    )
    home_btn.click()

    login_header = (By.XPATH, "//strong[contains(text(),'XYZ Bank')]")
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(login_header))
    assert "Bank" in driver.title or driver.find_element(*login_header).is_displayed(), "Home button did not navigate back"
    print("✅ Home button navigation successful")


@pytest.mark.login
def test_multiple_login_attempts(driver):
    """Verify multiple login attempts work properly"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.click_customer_login()
    users = ["Harry Potter", "Ron Weasly", "Hermoine Granger"]

    for user in users:
        try:
            login.select_user(user)
            login.click_login()
        except (StaleElementReferenceException, TimeoutException):
            driver.refresh()
            login.click_customer_login()
            login.select_user(user)
            login.click_login()

        logout_btn = (By.CSS_SELECTOR, "button[ng-click='byebye()']")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(logout_btn)).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Customer Login')]")))
        login.click_customer_login()

    print("✅ All customer login attempts successful")

