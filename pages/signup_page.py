from selenium.webdriver.common.by import By
from test_locators.locator import Locators

class Signup:
    def __init__(self, driver):
        self.driver = driver

    # Methods to interact with the signup page

    def click_signup(self):
        self.driver.find_element(*Locators.SIGNUP_LINK_XPATH).click()

    def enter_email(self, email):
        self.driver.find_element(*Locators.EMAIL_FIELD_ID).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*Locators.PASSWORD_FIELD_ID).send_keys(password)

    def click_continue(self):
        self.driver.find_element(*Locators.CONTINUE_BUTTON_XPATH).click()



