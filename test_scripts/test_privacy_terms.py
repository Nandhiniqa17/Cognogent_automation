import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.privacy_terms import Privacy, Privacy
from pages.login_page import Login
from pages.social_links import social_links
from test_data.test_data import TestData
from selenium import webdriver
from faker import Faker




@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Assuming you have ChromeDriver set up in PATH
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
@pytest.mark.specific
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Privacy Settings")
@allure.story("Verify Privacy Page Navigation")
@pytest.mark.order(9)
#@pytest.mark.skip(reason="Skipping this test case for now")
def test_privacy(setup):
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
        with allure.step("Navigate to Privacy Settings"):
         privacy = Privacy(driver)
        privacy.click_profile_setting()
        privacy.click_privacy()
        with allure.step("Save Privacy Page Screenshot"):
            driver.save_screenshot("screenshots\\Privacy.png")
            allure.attach.file("screenshots\\Privacy.png", name="Privacy Screenshot", attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed: {str(e)}")
@pytest.mark.specific
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Terms and Conditions")
@allure.story("Verify Terms Page Navigation")
@pytest.mark.order(10)
#@pytest.mark.skip(reason="Skipping this test case for now")
def test_terms(setup):
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
        with allure.step("Navigate to Terms Page"):
         privacy = Privacy(driver)
         privacy.click_profile_setting()
         privacy.click_termscon()
        with allure.step("Save Terms Page Screenshot"):
            driver.save_screenshot("screenshots\\Terms.png")
            allure.attach.file("screenshots\\Terms.png", name="Terms Screenshot", attachment_type=allure.attachment_type.PNG)


    except Exception as e:
        allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed: {str(e)}")