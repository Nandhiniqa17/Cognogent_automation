import time
import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from pages.login_page import Login
from test_data.test_data import TestData
from selenium import webdriver
from test_locators.locator import Locators


@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Assuming you have ChromeDriver set up in PATH
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.severity(allure.severity_level.BLOCKER)
@allure.feature('Login Feature')
@allure.story('Test login with previously registered user')
@pytest.mark.order(2)
@pytest.mark.specific
def test_login(setup):
    # Setup WebDriver
    with allure.step('Verify if test_data.json exists and load email'):
     test_data_file = "test_data.json"

    if not os.path.exists(test_data_file):
        allure.attach(test_data_file, name="test_data.json", attachment_type=allure.attachment_type.TEXT)
        pytest.fail("test_data.json not found. Ensure signup test has run first.")
    with allure.step('Load email from test data'):
     with open(test_data_file, "r") as f:
        data = json.load(f)
        signup_email = data.get("email")

    print(f"Running Login test with email: {signup_email}")

    driver = setup
    with allure.step('Navigate to Base URL'):
     driver.get(TestData.BASE_URL)

    with allure.step('Initialize Login page object'):
     login_page = Login(driver)
    # login_email = TestData.USERNAME
    # print(login_email)

    with allure.step('Enter credentials and login'):
     login_page.enter_username(TestData.USERNAME)
     login_page.enter_password(TestData.PASSWORD)
     login_page.click_continue()
     time.sleep(8)
    with allure.step('Verify Dashboard is displayed after login'):
     try:


        dashboard_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(Locators.DASHBOARD_XPATH
                                             ))
        assert dashboard_element.is_displayed(), "Dashboard element not visible after signup"
        allure.attach(driver.get_screenshot_as_png(), name="Dashboard Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        print(f"Login successful with email {signup_email}, Dashboard is displayed.")
     except Exception as e:
         allure.attach(driver.get_screenshot_as_png(), name="Login Failure Screenshot",
                       attachment_type=allure.attachment_type.PNG)
         pytest.fail(f"Login Test failed: {str(e)}")







