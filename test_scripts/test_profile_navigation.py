import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.privacy_terms import  Privacy
from pages.login_page import Login
from pages.profile_icon import ProfileIcon
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
@allure.feature("Profile Settings")
@allure.story("Test Profile Settings")
@pytest.mark.order(14)
@pytest.mark.skip(reason="Skipping this test case for now")
def test_profile_setting(setup):
    # Setup WebDriver
    driver = setup
    driver.get(TestData.BASE_URL)

    login_page = Login(driver)

    login_page.enter_username(TestData.USERNAME)
    login_page.enter_password(TestData.PASSWORD)
    login_page.click_continue()
    try:
        with allure.step("Navigating to Profile Settings"):
         profile = ProfileIcon(driver)
         profile.click_profile_icon()
         profile.click_profile_settings()
    except Exception as e:
        allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed due to: {e}")
@pytest.mark.order(15)
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Company Section")
@allure.story("Test Company Page")
@pytest.mark.skip(reason="Skipping this test case for now")
def test_company(setup):
    # Setup WebDriver
    driver = setup
    driver.get(TestData.BASE_URL)

    login_page = Login(driver)

    login_page.enter_username(TestData.USERNAME)
    login_page.enter_password(TestData.PASSWORD)
    login_page.click_continue()
    try:
        with allure.step("Navigating to Company Page"):
         profile = ProfileIcon(driver)
         profile.click_profile_icon()
         profile.click_company()

    except Exception as e:
        allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed due to: {e}")

@pytest.mark.order(16)
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Pricing Section")
@allure.story("Test Pricing Page")
@pytest.mark.skip(reason="Skipping this test case for now")
def test_pricing(setup):
    # Setup WebDriver
    driver = setup
    driver.get(TestData.BASE_URL)

    login_page = Login(driver)

    login_page.enter_username(TestData.USERNAME)
    login_page.enter_password(TestData.PASSWORD)
    login_page.click_continue()
    try:
        with allure.step("Navigating to Pricing Page"):
         profile = ProfileIcon(driver)
         profile.click_profile_icon()
         profile.click_pricing()
    except Exception as e:
        allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed due to: {e}")

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Blog Section")
@allure.story("Test Blog Page")
@pytest.mark.order(17)
@pytest.mark.skip(reason="Skipping this test case for now")
def test_blog(setup):
    # Setup WebDriver
    driver = setup
    driver.get(TestData.BASE_URL)

    login_page = Login(driver)

    login_page.enter_username(TestData.USERNAME)
    login_page.enter_password(TestData.PASSWORD)
    login_page.click_continue()
    try:
        with allure.step("Navigating to Blog Page"):
         profile = ProfileIcon(driver)
         profile.click_profile_icon()
         profile.click_blog()
    except Exception as e:
        allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed due to: {e}")

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Contact Us Section")
@allure.story("Test Contact Us Page")
@pytest.mark.order(11)
def test_contactus(setup):
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
        with allure.step("Navigating to profile icon"):
         profile = ProfileIcon(driver)
         profile.click_profile_icon()
         with allure.step("Navigating to Contact Us Page"):
          profile.click_contactus()
          allure.attach(driver.get_screenshot_as_png(), name="Contact Us Page Screenshot",
                        attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed due to: {e}")
