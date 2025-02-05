import json
import os
import time
import allure
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login
from pages.social_links import social_links
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
@pytest.mark.order(5)
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Session Management")
@allure.story("Create Session")
#@pytest.mark.specific
def test_session(setup):
        with allure.step("Read signup email from test_data.json"):
        # Setup WebDriver
         test_data_file = "test_data.json"

        if not os.path.exists(test_data_file):
            pytest.fail("test_data.json not found. Ensure signup test has run first.")

        with open(test_data_file, "r") as f:
            data = json.load(f)
            signup_email = data.get("email")

        print(f"Running Login test with email: {signup_email}")
        # Setup WebDriver
        driver = setup
        driver.get(TestData.BASE_URL)
        wait = WebDriverWait(driver, 30)
        login_page = Login(driver)
        with allure.step("Login with valid credentials"):
         login_page.enter_username(TestData.USERNAME)
         login_page.enter_password(TestData.PASSWORD)
         login_page.click_continue()
        time.sleep(10)
        with allure.step("Create new sessions "):
         try:

            session = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='w-7 h-7 rounded bg-[#2FA0A0] grid place-items-center']")))
            for i in range(5):
                session.click()
                time.sleep(5)
            popup = driver.find_element(*Locators.POPUP_XPATH)
            allure.attach(driver.get_screenshot_as_png(), name="popup_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            assert popup.is_displayed(), "Popup message not displayed."
         except Exception as e:
            pytest.fail(f"Test failed: {str(e)}")
@pytest.mark.order(6)
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test Session Delete")
@allure.description("Verifies that the session can be deleted successfully.")
#@pytest.mark.specific
def test_session_delete(setup):
    with allure.step("Read signup email from test_data.json"):
    # Setup WebDriver
     test_data_file = "test_data.json"

    if not os.path.exists(test_data_file):
        pytest.fail("test_data.json not found. Ensure signup test has run first.")

    with open(test_data_file, "r") as f:
        data = json.load(f)
        signup_email = data.get("email")

    print(f"Running Login test with email: {signup_email}")
    # Setup WebDriver
    driver = setup
    driver.get(TestData.BASE_URL)
    wait = WebDriverWait(driver, 30)
    login_page = Login(driver)
    with allure.step("Login with valid credentials"):
     login_page.enter_username(signup_email)
     login_page.enter_password(TestData.PASSWORD)
     login_page.click_continue()
    time.sleep(10)

    try:
        session_new = wait.until(EC.element_to_be_clickable(Locators.SESSION_PLUS_XPATH))
        session_new.click()

        with allure.step("Select session and click delete"):
         session = wait.until(EC.element_to_be_clickable(Locators.NEW_SESSION_XPATH))
         session.click()
         time.sleep(5)
         three_dots = wait.until(EC.visibility_of_element_located(Locators.THREE_DOTS_XPATH))
         three_dots.click()
         time.sleep(5)
         delete = wait.until(EC.element_to_be_clickable(Locators.DELETE_XPATH))
         delete.click()
         allure.attach(driver.get_screenshot_as_png(), name="deleted Session Screenshot",
                       attachment_type=allure.attachment_type.PNG)
         continue_btn = wait.until(EC.element_to_be_clickable(Locators.CONTINUE_XPATH))
         continue_btn.click()
         allure.attach(driver.get_screenshot_as_png(), name="deleted Session Screenshot",
                       attachment_type=allure.attachment_type.PNG)


    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test failed: {str(e)}")

@pytest.mark.order(7)
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test Session Edit")
@allure.description("Verifies that the session can be edited successfully.")
#@pytest.mark.specific
def test_session_edit(setup):
    with allure.step("Read signup email from test_data.json"):
    # Setup WebDriver
     test_data_file = "test_data.json"

    if not os.path.exists(test_data_file):
        pytest.fail("test_data.json not found. Ensure signup test has run first.")

    with open(test_data_file, "r") as f:
        data = json.load(f)
        signup_email = data.get("email")

    print(f"Running Login test with email: {signup_email}")
    # Setup WebDriver
    driver = setup
    driver.get(TestData.BASE_URL)
    wait = WebDriverWait(driver, 30)
    login_page = Login(driver)
    with allure.step("Login with valid credentials"):
     login_page.enter_username(signup_email)
     login_page.enter_password(TestData.PASSWORD)
     login_page.click_continue()
     time.sleep(10)

    try:
        with allure.step("Edit session name"):
         session = wait.until(EC.element_to_be_clickable(Locators.NEW_SESSION_XPATH))

         session.click()
         time.sleep(5)
         three_dots = wait.until(EC.visibility_of_element_located(Locators.THREE_DOTS_XPATH))
         three_dots.click()
         time.sleep(5)

         edit = wait.until(EC.element_to_be_clickable(Locators.EDIT_XPATH))
         edit.click()
         time.sleep(5)
         session_name = wait.until(EC.visibility_of_element_located(Locators.SESSION_NAME_XPATH))
         time.sleep(2)
         session_name.clear()
         session_name.send_keys(TestData.SESSION_NAME)
         session_name.send_keys(Keys.ENTER)
         time.sleep(5)
         driver.save_screenshot("screenshots\\edit_session.png")
         click_session = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='w-7 h-7 rounded bg-[#2FA0A0] grid place-items-center']")))
         click_session.click()
         allure.attach(driver.get_screenshot_as_png(), name="Edited Session Screenshot",
                       attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test failed: {str(e)}")