import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import Home
from pages.login_page import Login
from test_data.test_data import TestData
from selenium import webdriver



@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Assuming you have ChromeDriver set up in PATH
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Home Page")
@allure.story("Verify Dashboard and Menu List")
@pytest.mark.order(8)
def test_home(setup):
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
        with allure.step("Navigate to Dashboard"):
         home = Home(driver)
         time.sleep(5)
         home.click_dashboard()
        with allure.step("Verify Menu List"):
         home.menu_list()
        allure.attach(driver.get_screenshot_as_png(), name="Home Page Screenshot",
                      attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        with allure.step("Capture Failure Screenshot"):
            screenshot_path = "screenshots\\Failed_Home_Test.png"
            driver.save_screenshot(screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="Failed Test Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed: {str(e)}")