import time

from selenium.webdriver.common.by import By
from test_locators.locator import Locators

class social_links:
    def __init__(self, driver):
        self.driver = driver
    def click_linkedin(self):
        main_window = self.driver.current_window_handle
        self.driver.find_element(*Locators.LINKEDIN_XPATH).click()
        window_handles = self.driver.window_handles
        for handle in window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break
        time.sleep(8)
        # Get the title of the current page
        page_title = self.driver.title
        print(page_title)

        # Assert that the page title contains 'LinkedIn'
        assert "Cognogent | LinkedIn" in page_title, f"Page title does not contain 'LinkedIn'. Actual title: {page_title}"
        # Print success message if assertion passes
        print("Assertion passed: Page title contains 'LinkedIn'.")
        self.driver.switch_to.window(main_window)

    def click_youtube(self):
        main_window = self.driver.current_window_handle
        self.driver.find_element(*Locators.YOUTUBE_XPATH).click()
        window_handles = self.driver.window_handles
        for handle in window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break
        time.sleep(10)
        page_title = self.driver.title
        print(page_title)

        # Assert that the page title contains 'LinkedIn'
        assert "YouTube" in page_title, f"Page title does not contain 'Youtube'. Actual title: {page_title}"

        # Print success message if assertion passes
        print("Assertion passed: Page title contains 'Youtube'.")
        self.driver.save_screenshot("screenshots\\youtube.png")
        self.driver.switch_to.default_content()