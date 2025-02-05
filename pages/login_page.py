from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from test_locators.locator import Locators

class Login:
    def __init__(self, driver):
        self.driver = driver

    # Methods to interact with the signup page



    def enter_username(self, email):
        self.driver.find_element(*Locators.Username_ID).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*Locators.Password_ID).send_keys(password)

    def click_continue(self):
        self.driver.find_element(*Locators.CONTINUE_BUTTON_XPATH).click()

    def upload(self, path):
        self.driver.find_element(*Locators.FILE_UPLOAD_XPATH).send_keys(path)
    def submit(self):
        submit = self.driver.find_element(*Locators.SUBMIT_BUTTON_XPATH)
        action =ActionChains(self.driver)
        action.move_to_element(submit).click().perform()

        #self.driver.execute_script("arguments[0].scrollIntoView();", submit)

