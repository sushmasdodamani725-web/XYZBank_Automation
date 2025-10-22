from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "username")  # Replace with actual site IDs
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")

class CustomerLocators:
    ADD_CUSTOMER_BTN = (By.ID, "addCustomer")
    NAME_FIELD = (By.ID, "customerName")
    EMAIL_FIELD = (By.ID, "customerEmail")
    BALANCE_FIELD = (By.ID, "customerBalance")
    SAVE_BTN = (By.ID, "saveCustomer")

class TransactionLocators:
    DEPOSIT_BTN = (By.ID, "depositBtn")
    WITHDRAW_BTN = (By.ID, "withdrawBtn")
    AMOUNT_FIELD = (By.ID, "amount")
    SUBMIT_BTN = (By.ID, "submitTransaction")
