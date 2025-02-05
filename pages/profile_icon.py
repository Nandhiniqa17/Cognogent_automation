import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_locators.locator import Locators


class ProfileIcon:
    def __init__(self, driver):
        self.driver = driver
    def click_profile_icon(self):
        self.driver.find_element(*Locators.PROFILE_IMAGE_XPATH).click()

    # def click_profile_settings(self):
    #     #main_window = self.driver.current_window_handle
    #     profile_settings = self.driver.find_element(By.XPATH,SignupLocators.PROFILE_SETTINGS_XPATH)
    #     profile_settings.click()
    #     # window_handles =self.driver.window_handles
    #     # for handle in window_handles:
    #     #     if handle != main_window:
    #     #         self.driver.switch_to.window(handle)
    #     #         break
    #     # signin = self.driver.find_element(By.XPATH, '// a[text() = "Sign In"]')
    #     # signin.click()
    #     self.driver.save_screenshot("screenshots\\Profile_settings.png")
    #     self.driver.close()
    #     #self.driver.switch_to.window(main_window)
    #     self.driver.find_element(By.XPATH, SignupLocators.PROFILE_IMAGE_XPATH).click()
    #     main_window = self.driver.current_window_handle
    #     profile = self.driver.find_element(By.XPATH, SignupLocators.PROFILE_SETTINGS_XPATH)
    #     profile.click()
    #     window_handles = self.driver.window_handles
    #     for handle in window_handles:
    #         if handle != main_window:
    #             self.driver.switch_to.window(handle)
    #             break
    #     #Address details
    #     time.sleep(5)
    #     close_chat = self.driver.find_element(By.XPATH,"//button[@aria-label='Close live chat']")
    #     close_chat.click()
    #     address_edit_btn = self.driver.find_element(By.XPATH,"(//button[contains(@class, 'btn-outline-secondary') and contains(span, 'Edit/Add')])[1]")
    #     address_edit_btn.click()
    #     country_data = "India"
    #     country = self.driver.find_element(By.XPATH,'//input[@id="Country"]')
    #     country.send_keys(country_data)
    #     add_btn = self.driver.find_element(By.XPATH,'//button[text()="update"]')
    #     add_btn.click()
    #     #Company details
    #     company_edit_btn = self.driver.find_element(By.XPATH,"(//button[contains(@class, 'btn-outline-secondary') and contains(span, 'Edit/Add')])[2]")
    #     company_edit_btn.click()
    #     company_name = self.driver.find_element(By.XPATH,'//input[@id="Company"]')
    #     company_name.send_keys("Cognogent")
    #     add_btn = self.driver.find_element(By.XPATH,'//button[text()="Add"]')
    #     add_btn.click()
    #     self.driver.save_screenshot("Profile_information.png")
    #     text_data = self.driver.find_element(By.XPATH,'//h5[text()="India"]')
    #     if text_data.text == country_data:
    # #         print("Country added successfully")
    #
    #
    #
    # def click_company(self):
    #
    #     main_window = self.driver.current_window_handle
    #
    #     company = self.driver.find_element(By.XPATH, "//a[@href='https://qa-marketing.cognogent.com/company']")
    #     company.click()
    #     time.sleep(6)
    #     window_handles = self.driver.window_handles
    #     for handle in window_handles:
    #         if handle != main_window:
    #             self.driver.switch_to.window(handle)
    #             break
    #
    #     self.driver.save_screenshot("screenshots\\Company.png")
    #     time.sleep(10)
    #
    # def click_pricing(self):
    #     main_window = self.driver.current_window_handle
    #     wait = WebDriverWait(self.driver, 10)
    #     company = self.driver.find_element(By.XPATH, "//a[@href='https://qa-marketing.cognogent.com/pricing']")
    #     company.click()
    #     time.sleep(6)
    #     window_handles = self.driver.window_handles
    #     for handle in window_handles:
    #         if handle != main_window:
    #             self.driver.switch_to.window(handle)
    #             break
    #
    #     self.driver.save_screenshot("screenshots\\pricing.png")
    #     time.sleep(10)
    #     wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="CONTACT US"]'))).click()
    #     # driver.find_element(By.XPATH,'//button[text()="CONTACT US"]').click()
    #     self.driver.save_screenshot("screenshots\\contactus.png")
    #
    #
    # def click_blog(self):
    #     main_window = self.driver.current_window_handle
    #
    #     blog = self.driver.find_element(By.XPATH, "//a[@href='https://qa-marketing.cognogent.com/blog']")
    #     blog.click()
    #     time.sleep(6)
    #     window_handles = self.driver.window_handles
    #     for handle in window_handles:
    #         if handle != main_window:
    #             self.driver.switch_to.window(handle)
    #             break
    #
    #     self.driver.save_screenshot("screenshots\\blog.png")

    def click_contactus(self):
        main_window = self.driver.current_window_handle

        contact_us = self.driver.find_element(*Locators.CONTACT_US_XPATH)
        contact_us.click()
        time.sleep(6)
        window_handles = self.driver.window_handles
        for handle in window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

        self.driver.save_screenshot("screenshots\\contact_us.png")