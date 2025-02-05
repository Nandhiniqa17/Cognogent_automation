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
@allure.feature("File Upload Test")
@allure.story("User should be able to upload a file and verify elements")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.specific
def test_file_upload(setup):
    test_data_file = "test_data.json"

    if not os.path.exists(test_data_file):
        pytest.fail("test_data.json not found. Ensure signup test has run first.")

    with open(test_data_file, "r") as f:
        data = json.load(f)
        signup_email = data.get("email")

    print(f"Running Login test with email: {signup_email}")
    # Setup WebDriver
    allure.step("Running Login test with email: {0}".format(signup_email))
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
    #print(f"Signup successful with email {signup_email}, Dashboard is displayed.")
    # file_path = TestData.File_path
    # print(f"File path for upload: {file_path}")  # Debugging step to verify file path  
    with allure.step("Uploading file"):
    # Wait for the file upload element to be clickable
     try:
        time.sleep(10)
        session = wait.until(EC.element_to_be_clickable(Locators.SESSION_XPATH))
        session.click()
        #time.sleep(15)
        file_input = driver.find_element(*Locators.FILE_UPLOAD_XPATH)
        driver.execute_script("arguments[0].style.display = 'block';", file_input)
        with allure.step("FileUploaded"):
         file_input.send_keys(r"C:\\Cognogent_data\\NIST_Sources_Sought_Notice_HPC-Final.docx")
        time.sleep(30)
        login_page.submit()
        time.sleep(180)
        driver.save_screenshot("screenshots\\SingleFileUpload.png")
        allure.attach(driver.get_screenshot_as_png(), name=" Single File Upload Screenshot",
                      attachment_type=allure.attachment_type.PNG)

        with allure.step("Verifying compliance checklist, win theme, and storyboard"):
         compliance = driver.find_element(*Locators.COMPLIANCE_CHECKLIST_XPATH)
         wintheme = driver.find_element(*Locators.WIN_THEME_XPATH)
         story_board = driver.find_element(*Locators.STORY_BOARD_XPATH)
         assert compliance.is_displayed() and wintheme.is_displayed() and story_board.is_displayed(), "Required elements are not displayed"
        # if compliance.is_displayed() and wintheme.is_displayed() and story_board.is_displayed():
        #     print("Compliance checklist, win theme and story board displayed")

     except TimeoutException:
        # Debugging message if the element wasn't found
        print("File upload element not found within the timeout")
        assert False, "File upload element not found"


@pytest.mark.order(3)
@allure.feature("Multiple File Upload Test")
@allure.story("User should be able to upload multiple files simultaneously and verify elements")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.specific
def test_multiple_file_uploads(setup):
    test_data_file = "test_data.json"

    if not os.path.exists(test_data_file):
        pytest.fail("test_data.json not found. Ensure signup test has run first.")

    with open(test_data_file, "r") as f:
        data = json.load(f)
        signup_email = data.get("email")

    print(f"Running Login test with email: {signup_email}")
    allure.step("Running Login test with email: {0}".format(signup_email))
    driver = setup
    driver.get(TestData.BASE_URL)
    wait = WebDriverWait(driver, 30)
    login_page = Login(driver)

    # Logging in
    with allure.step("Entering login credentials"):
        login_page.enter_username(signup_email)
        login_page.enter_password(TestData.PASSWORD)
        login_page.click_continue()

    with allure.step("Validating dashboard visibility"):
        dashboard_element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.DASHBOARD_XPATH))

        assert dashboard_element.is_displayed(), "Dashboard element not visible after login"

    # File paths to upload
    file_paths = [
        r"C:\\Cognogent_data\\RFQ_Final.pdf",
        r"C:\\Cognogent_data\\NIST_Sources_Sought_Notice_HPC-Final.docx",

    ]

    file_paths_combined = "\n".join(file_paths)  # Combine paths for simultaneous upload

    with allure.step("Uploading multiple files simultaneously"):
        try:
            time.sleep(10)
            session = wait.until(EC.element_to_be_clickable(Locators.SESSION_XPATH))
            session.click()
            time.sleep(6)

            # Make the file input element visible for automation
            file_input = driver.find_element(*Locators.FILE_UPLOAD_XPATH)
            driver.execute_script("arguments[0].style.display = 'block';", file_input)

            # Upload all files at once
            file_input.send_keys(file_paths_combined)
            time.sleep(180)
            login_page.submit()
            time.sleep(180)
            driver.save_screenshot("screenshots\\after_multiple_file_upload.png")
            allure.attach(driver.get_screenshot_as_png(), name="Multiple File Screenshot",
                          attachment_type=allure.attachment_type.PNG)

            with allure.step("Verifying compliance checklist, win theme, and storyboard"):
                compliance = driver.find_element(*Locators.COMPLIANCE_CHECKLIST_XPATH)
                wintheme = driver.find_element(*Locators.WIN_THEME_XPATH)
                story_board = driver.find_element(*Locators.STORY_BOARD_XPATH)
                assert (
                    compliance.is_displayed() and
                    wintheme.is_displayed() and
                    story_board.is_displayed()
                ), "Required elements are not displayed after uploading files"
                print(f"All files uploaded successfully and elements verified")

        except TimeoutException:
            print("File upload element not found for the provided files")
            assert False, "File upload element not found for the provided files"






























    # Upload the file

    # Get the full path of the file to upload
    # file_path = os.path.abspath(TestData.File_path)
    # upload = wait.until(EC.element_to_be_clickable((By.XPATH, SignupLocators.FILE_UPLOAD_XPATH)))
    # upload.send_keys(file_path)
    # #login_page.upload(file_path)
    # time.sleep(10)
    # login_page.submit()
    # driver.save_screenshot("screenshots/file_upload.png")

    # Locate the file upload input element and upload the file


    # Optionally, you can add assertions to check if the file upload was successful
    # For example, you can verify the name of the uploaded file is displayed somewhere on the page
 # upload_element = wait.until(
        #     EC.presence_of_element_located((By.XPATH, SignupLocators.FILE_UPLOAD_XPATH)))
        # driver.execute_script("arguments[0].style.display = 'block';", upload_element)
        # upload_element.send_keys(file_path)