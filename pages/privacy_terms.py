import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from test_locators.locator import Locators


class Privacy:
    def __init__(self, driver):
        self.driver = driver

    def click_profile_setting(self):
        self.driver.find_element(*Locators.PROFILE_IMAGE_XPATH).click()
        main_window = self.driver.current_window_handle
        contact_us = self.driver.find_element(*Locators.CONTACT_US_XPATH)
        contact_us.click()
        window_handles =self.driver.window_handles
        for handle in window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

        self.driver.save_screenshot("screenshots\\profile.png")
    def click_privacy(self):
        privacy_element=self.driver.find_element(*Locators.PRIVACY_XPATH)
        actions = ActionChains(self.driver)
        actions.move_to_element(privacy_element).click().perform()
        time.sleep(10)
        page_title = self.driver.title
        print(f"Page title: {page_title}")

        # Assert that the page title contains 'Privacy'
        assert "Privacy" in page_title, f"Page title does not contain 'Privacy'. Actual title: {page_title}"

        # Print success message if the assertion passes
        print("Assertion passed: Page title contains 'Privacy'.")

    def click_termscon(self):
        terms_element= self.driver.find_element(*Locators.TERMS_XPATH)
        actions = ActionChains(self.driver)
        actions.move_to_element(terms_element).click().perform()
        time.sleep(8)
        page_title = self.driver.title
        print(f"Page title: {page_title}")

        # Assert that the page title contains 'Privacy'
        assert "Termsofuse" in page_title, f"Page title does not contain 'Termsofuse'. Actual title: {page_title}"


        # Print success message if the assertion passes
        print("Assertion passed: Page title contains 'Termsofuse'.")