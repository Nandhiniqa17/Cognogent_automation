import json
import time
import allure
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from test_locators.locator import Locators
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import Login
from test_data.test_data import TestData
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Assuming you have ChromeDriver set up in PATH
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.order(4)
@allure.feature("File Upload and Session Deletion Test")
@allure.story("User should be able to upload a file, verify elements, and delete session")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.specific
def test_file_upload_and_session_delete(setup):
    test_data_file = "test_data.json"

    if not os.path.exists(test_data_file):
        pytest.fail("test_data.json not found. Ensure signup test has run first.")

    with open(test_data_file, "r") as f:
        data = json.load(f)
        signup_email = data.get("email")

    # Use the provided username and password
    username = "nandhinis@yopmail.com"
    password = "Password@123"

    print(f"Running Login test with email: {signup_email}")
    # Setup WebDriver
    driver = setup
    driver.get(TestData.BASE_URL)
    wait = WebDriverWait(driver, 30)
    login_page = Login(driver)

    with allure.step("Entering login credentials"):
        login_page.enter_username(TestData.USERNAME)
        login_page.enter_password(TestData.PASSWORD)
        login_page.click_continue()
        time.sleep(8)

    with allure.step("Validating dashboard visibility"):
        dashboard_element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.DASHBOARD_XPATH))
        assert dashboard_element.is_displayed(), "Dashboard element not visible after signup"

    with allure.step("Uploading file"):
        # Wait for the file upload element to be clickable
        try:
            time.sleep(5)
            session = wait.until(EC.element_to_be_clickable(Locators.SESSION_XPATH))
            session.click()
            file_input = driver.find_element(*Locators.FILE_UPLOAD_XPATH)
            driver.execute_script("arguments[0].style.display = 'block';", file_input)
            file_input.send_keys(r"C:\\Cognogent_data\\NIST_Sources_Sought_Notice_HPC-Final.docx")
            time.sleep(8)
            login_page.submit()
            time.sleep(10)
            driver.save_screenshot("screenshots\\SingleFileUpload.png")
            allure.attach(driver.get_screenshot_as_png(), name="Single File Upload Screenshot", attachment_type=allure.attachment_type.PNG)

            with allure.step("Verifying compliance checklist, win theme, and storyboard"):
                compliance = driver.find_element(*Locators.COMPLIANCE_CHECKLIST_XPATH)
                wintheme = driver.find_element(*Locators.WIN_THEME_XPATH)
                story_board = driver.find_element(*Locators.STORY_BOARD_XPATH)
                assert compliance.is_displayed() and wintheme.is_displayed() and story_board.is_displayed(), "Required elements are not displayed"

        except TimeoutException:
            # Debugging message if the element wasn't found
            print("File upload element not found within the timeout")
            assert False, "File upload element not found"

    with allure.step("Deleting the session"):
        try:
            # Start the session deletion process
            three_dots = wait.until(EC.visibility_of_element_located(Locators.THREE_DOTS_XPATH))
            three_dots.click()
            time.sleep(5)
            delete = wait.until(EC.element_to_be_clickable(Locators.DELETE_XPATH))
            delete.click()
            allure.attach(driver.get_screenshot_as_png(), name="Deleted Session Screenshot", attachment_type=allure.attachment_type.PNG)

            continue_btn = wait.until(EC.element_to_be_clickable(Locators.CONTINUE_XPATH))
            continue_btn.click()
            allure.attach(driver.get_screenshot_as_png(), name="Deleted Session Screenshot After Continue", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
            pytest.fail(f"Test failed during session deletion: {str(e)}")
