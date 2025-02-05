import logging
import time
from os import times

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login
from test_data.test_data import TestData
from test_locators.locator import Locators

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Assuming you have ChromeDriver set up in PATH
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.feature("Theme Selection")
@allure.story("Test Light Theme")
@pytest.mark.order(14)
def test_light_theme(setup, signup_email):
    driver = setup
    driver.get(TestData.BASE_URL)
    wait = WebDriverWait(driver, 10)

    # Perform the login process with the given email (signup_email)
    # Replace the following with your actual login steps
    logging.info("Logging in with email: %s", signup_email)
    login_page = Login(driver)
    login_page.enter_username(TestData.USERNAME)
    login_page.enter_password(TestData.PASSWORD)
    login_page.click_continue()

    # After successful login, we now select the theme
    logging.info("Selecting light theme...")

    # Wait for the theme element to be visible and click it
    theme = wait.until(EC.visibility_of_element_located(Locators.LIGHT_THEME))
    theme.click()
    time.sleep(5)
    driver.save_screenshot("screenshots\\light_theme.png")
    allure.attach(driver.get_screenshot_as_png(), name="Light theme Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    logging.info("Selecting dark theme...")
    time.sleep(8)
    dark_theme = wait.until(
        EC.visibility_of_element_located(Locators.DARK_THEME))
    dark_theme.click()
    driver.save_screenshot("screenshots\\dark_theme1.png")
    allure.attach(driver.get_screenshot_as_png(), name="Dark theme Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    logging.info("Theme selected successfully.")





















# @allure.feature("Theme Selection")
# @allure.story("Test Dark Theme")
# @pytest.mark.order(7)
# def test_dark_theme(setup, signup_email):
#     driver = setup
#     driver.get(TestData.BASE_URL)
#     wait = WebDriverWait(driver, 10)
#
#         # Perform the login process with the given email (signup_email)
#         # Replace the following with your actual login steps
#     logging.info("Logging in with email: %s", signup_email)
#     login_page = Login(driver)
#     login_page.enter_username(TestData.USERNAME)
#     login_page.enter_password(TestData.PASSWORD)
#     login_page.click_continue()
#
#         # After successful login, we now select the theme
#
#
#         # Wait for the theme element to be visible and click it
#     dark_theme = wait.until(
#         EC.visibility_of_element_located((By.XPATH, '//div[@class="w-5.5 h-5.5 rounded-[10px] p-1 bg-[#64666D]"]')))
#     dark_theme.click()
#     driver.save_screenshot("screenshots\\dark_theme.png")
#
#
#
#
#     # Add assertions or further steps after theme selection
#
