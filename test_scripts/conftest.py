from pathlib import Path

import pytest
import os
import json
from faker import Faker

# Path to your test data file
TEST_DATA_FILE = "test_data.json"

@pytest.fixture(scope="session")
def signup_email(request):
    """Fixture to generate the signup email and store it in a JSON file."""
    fake = Faker()
    email = fake.email()
    print(f"Generated email: {email}")

    # Remove any existing file before creating a new one
    if os.path.exists(TEST_DATA_FILE):
        os.remove(TEST_DATA_FILE)

    # Write the email to the JSON file
    with open(TEST_DATA_FILE, "w") as f:
        json.dump({"email": email}, f)

    # Yield the email to be used in the tests
    yield email

    # No cleanup is required, as the file should not be deleted after the tests.
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshot to the HTML report for failed tests."""
    if call.when == "call" and call.excinfo is not None:
        # Get the WebDriver from the test fixture
        driver = item.funcargs.get("setup")  # Use the fixture name from your test (e.g., "setup")
        if driver:
            # Log to check if this hook is being called
            print(f"Test failed: {item.nodeid}")

            # Define the absolute path for the screenshot directory
            screenshot_dir = "/screenshots"
            Path(screenshot_dir).mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

            # Define the full path for the screenshot file
            screenshot_path = f"{screenshot_dir}/{item.nodeid.replace('::', '_').replace('/', '_')}_Failure.png"
            print(f"Saving screenshot to: {screenshot_path}")

            # Save the screenshot
            driver.save_screenshot(screenshot_path)