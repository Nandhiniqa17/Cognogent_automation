import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login
from pages.social_links import social_links
from test_data.test_data import TestData
from selenium import webdriver
from faker import Faker

from test_locators.locator import Locators


@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Assuming you have ChromeDriver set up in PATH
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Social Media Links")
@allure.story("Verify LinkedIn Link Navigation")
@pytest.mark.order(12)
def test_linkedin(setup):
    # Setup WebDriver
    driver = setup
    driver.get(TestData.BASE_URL)

    login_page = Login(driver)
    with allure.step("Enter Username and Password"):
     login_page.enter_username(TestData.USERNAME)
     login_page.enter_password(TestData.PASSWORD)
    with allure.step("Click Continue to Login"):
     login_page.click_continue()


    try:
        with allure.step("Navigate to LinkedIn"):
         links = social_links(driver)
         links.click_linkedin()
        allure.attach(driver.get_screenshot_as_png(), name="LinkedIn Screenshot",
                      attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        print(f"Assertion failed: {e}")
        driver.save_screenshot("AssertionFailed_Linkedin.png")

@pytest.mark.order(13)
def test_youtube(setup):
    # Setup WebDriver
    driver = setup
    driver.get(TestData.BASE_URL)

    login_page = Login(driver)
    with allure.step("Enter Username and Password"):
     login_page.enter_username(TestData.USERNAME)
     login_page.enter_password(TestData.PASSWORD)
    with allure.step("Click Continue to Login"):
     login_page.click_continue()

    try:
        with allure.step("Navigate to YouTube link"):
         links = social_links(driver)
         links.click_youtube()
        allure.attach(driver.get_screenshot_as_png(), name="Youtube Screenshot",
                      attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        print(f"Assertion failed: {e}")
        driver.save_screenshot("AssertionFailed_Youtube.png")