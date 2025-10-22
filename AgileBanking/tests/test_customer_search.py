import pytest
from pages.login_page import LoginPage
from pages.customer_search import CustomerSearchPage

BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

@pytest.mark.customer_search
def test_search_customer(driver):
    # Step 1: Open and login as Bank Manager
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.click_bank_manager_login()

    # Step 2: Open Customers tab
    search_page = CustomerSearchPage(driver)
    search_page.open_customers_tab()

    # Step 3: Search for a known customer
    customer_name = "Harry"  # existing demo customer
    search_page.search_customer(customer_name)

    # Step 4: Verify that searched customer appears
    displayed_customers = search_page.get_displayed_customers()
    assert any(customer_name in c for c in displayed_customers), f"{customer_name} not found in results"

    print(f"✅ Customer search successful for: {customer_name}")
