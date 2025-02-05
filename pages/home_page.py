import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_data.test_data import TestData
from test_locators.locator import Locators

class Home:
    def __init__(self, driver):
        self.driver = driver
    def click_dashboard(self):
        main_window = self.driver.current_window_handle
        self.driver.find_element(*Locators.HOME_PAGE_XPATH).click()
        window_handles = self.driver.window_handles
        for handle in window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break
        time.sleep(5)
        self.driver.save_screenshot("screenshots\\home_page.png")
    def menu_list(self):

        ul_element = self.driver.find_element(*Locators.UL_ELEMENT_XPATH)
        # Find all <li> elements within the <ul>
        li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
        # Loop through each menu item and check if it's displayed in the list
        for item in TestData.MENU_LIST:
            found = False
            for li in li_elements:
                # Check if the text of the <a> element within <li> matches the menu item
                if item in li.text:
                    found = True
                    print(f"Menu item '{item}' is displayed.")
                    break
            if not found:
                print(f"Menu item '{item}' is NOT displayed.")
        accept_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.ACCEPT_BUTTON_XPATH)
        )
        if accept_button.is_displayed():
            accept_button.click()
            print("Accept button clicked.")

        # If the button is present, click it

