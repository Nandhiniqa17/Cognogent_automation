# test_signup.py
import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.signup_page import Signup
from test_data.test_data import TestData
from selenium import webdriver
from pages.login_page import Login
from test_locators.locator import Locators


@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Assuming you have ChromeDriver set up in PATH
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature('Signup Feature')
@allure.story('Test signup with valid credentials')
@pytest.mark.order(1)
@pytest.mark.specific
def test_signup(setup,signup_email):
    # Setup WebDriver
    with allure.step('Setup WebDriver and Navigate to Base URL'):
      driver = setup
      driver.get(TestData.BASE_URL)
        # Initialize the SignupPage object
    with allure.step('Initialize Signup page object'):
      signup_page = Signup(driver)

    # Interact with the signup page
    with allure.step('Click on Signup and Enter Credentials'):
      signup_page.click_signup()
      email = signup_email

      signup_page.enter_email(email)
      signup_page.enter_password(TestData.PASSWORD)
      signup_page.click_continue()
      time.sleep(20)

    with allure.step('Verify Dashboard is displayed after signup'):
     try:


        dashboard_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(Locators.DASHBOARD_XPATH
        ))
        assert dashboard_element.is_displayed(), "Dashboard element not visible after signup"
        allure.attach(driver.get_screenshot_as_png(), name="Dashboard Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        print(f"Signup successful with email {signup_email}, Dashboard is displayed.")
     except Exception as e:
         allure.attach(driver.get_screenshot_as_png(), name="Signup Failure Screenshot",
                       attachment_type=allure.attachment_type.PNG)
         pytest.fail(f"Signup Test failed: {str(e)}")

