# # import pytest
# # from pages.transaction import CustomerTransactionPage
# # from pages.login_page import LoginPage
# #
# # BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
# #
# # @pytest.mark.transaction
# # def test_customer_transaction_flow(driver):
# #     login_page = LoginPage(driver)
# #     login_page.open(BASE_URL)
# #
# #     # --- Step 1: Login as Customer ---
# #     transaction_page = CustomerTransactionPage(driver)
# #     customer_name = "Harry Potter"  # This name exists in the demo site
# #     transaction_page.login_as_customer(customer_name)
# #
# #     # --- Step 2: Deposit Money ---
# #     deposit_message = transaction_page.deposit("1000")
# #     assert "Deposit Successful" in deposit_message, "Deposit failed!"
# #     print("✅ Deposit successful.")
# #
# #     # --- Step 3: Check Balance after Deposit ---
# #     balance_after_deposit = transaction_page.get_balance()
# #     print(f"Balance after deposit: {balance_after_deposit}")
# #     assert int(balance_after_deposit) >= 1000, "Balance not updated after deposit!"
# #
# #     # --- Step 4: Withdraw Money ---
# #     withdraw_message = transaction_page.withdraw("500")
# #     assert "Transaction successful" in withdraw_message, "Withdrawal failed!"
# #     print("✅ Withdrawal successful.")
# #
# #     # --- Step 5: Check Balance after Withdrawal ---
# #     balance_after_withdraw = transaction_page.get_balance()
# #     print(f"Balance after withdrawal: {balance_after_withdraw}")
# #     assert int(balance_after_withdraw) == int(balance_after_deposit) - 500, "Incorrect balance after withdrawal!"
# #
# #     # --- Step 6: Logout ---
# #     transaction_page.logout()
# #     assert "customer" in driver.current_url.lower(), "Logout unsuccessful!"
# #     print("✅ Customer logout successful.")
# import pytest
# from pages.login_page import LoginPage
# from pages.transaction import CustomerTransactionPage
#
# BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
#
# @pytest.mark.transaction
# def test_customer_transaction_flow(driver):
#     # Step 1: Open and login
#     login_page = LoginPage(driver)
#     login_page.open(BASE_URL)
#
#     transaction_page = CustomerTransactionPage(driver)
#     transaction_page.login_as_customer("Harry Potter")
#
#     # Step 2: Perform deposit
#     transaction_page.perform_deposit(500)
#
#     # Step 3: Open and reset transactions
#     transaction_page.open_transactions()
#     transaction_page.reset_transactions()
#
#     # Step 4: Logout
#     # transaction_page.logout()
#     #
#     # assert "login" in driver.current_url or "#/login" in driver.current_url, "Customer logout failed"
