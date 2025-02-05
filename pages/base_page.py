# base_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator_type, locator_value):
        """Reusable method to find elements."""
        return self.driver.find_element(locator_type, locator_value)

    def send_keys(self, locator_type, locator_value, text):
        """Reusable method to send keys to an element."""
        element = self.find_element(locator_type, locator_value)
        element.send_keys(text)

    def click(self, locator_type, locator_value):
        """Reusable method to click on an element."""
        element = self.find_element(locator_type, locator_value)
        element.click()
