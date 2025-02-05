import subprocess
import os
import shutil

ALLURE_RESULTS_DIR = "allure-results"
ALLURE_REPORT_DIR = "allure-report"
ALLURE_HTML_FILE = "index.html"


def create_directory(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def run_pytest():
    """Run pytest with Allure options for multiple test files."""
    create_directory(ALLURE_RESULTS_DIR)
    pytest_command = [
        "pytest",
        "--alluredir", ALLURE_RESULTS_DIR,  # Path for Allure results
        "test_scripts/"  # Run all tests in the test_scripts directory
    ]
    try:
        subprocess.run(pytest_command, check=True)
        print("Pytest execution completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during pytest execution: {e}")


def generate_allure_report():
    """Generate the Allure report from the results directory."""
    allure_generate_command = [
        "allure",
        "generate",
        ALLURE_RESULTS_DIR,
        "-o", ALLURE_REPORT_DIR,
        "--clean"
    ]
    try:
        subprocess.run(allure_generate_command, check=True)
        print("Allure report generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Allure report generation: {e}")


def convert_report_to_html():
    """Convert Allure report to a single .html file."""
    if not os.path.exists(ALLURE_REPORT_DIR):
        print("Allure report directory does not exist. Cannot convert to HTML.")
        return
    try:
        # Convert the Allure report to a single HTML file using Puppeteer
        convert_command = [
            "npx",
            "puppeteer",
            "screenshot",
            f"file://{os.path.abspath(ALLURE_REPORT_DIR)}/index.html",
            "--output",
            ALLURE_HTML_FILE
        ]
        subprocess.run(convert_command, check=True)
        print(f"Allure report converted to {ALLURE_HTML_FILE}.")
    except subprocess.CalledProcessError as e:
        print(f"Error during HTML conversion: {e}")


run_pytest()
generate_allure_report()
convert_report_to_html()

# import subprocess
# import os
#
# # Define Allure Results Directory
# ALLURE_RESULTS_DIR = "allure-results"
#
# def create_directory(directory):
#     """
#     Create directory if it doesn't exist.
#     """
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
# def run_pytest():
#     """
#     Run pytest with Allure options for multiple test files.
#     """
#     # Ensure the Allure Results directory exists
#     create_directory(ALLURE_RESULTS_DIR)
#
#     # Pytest command to run tests and generate Allure results
#     pytest_command = [
#         "pytest",
#         "--alluredir", ALLURE_RESULTS_DIR,  # Path for Allure results
#         "test_scripts/test_signup.py",      # Update with relative paths to test scripts
#         "test_scripts/test_login.py",
#         "test_scripts/test_profile_navigation.py",
#         "test_scripts/test_privacy_terms.py",
#         "test_scripts/test_session.py",
#         "test_scripts/test_fileupload.py",
#         "test_scripts/test_home_page.py",
#         "test_scripts/test_social_links.py",
#         "test_scripts/test_session.py",
#         "test_scripts/test_theme.py"
#     ]
#
#     try:
#         subprocess.run(pytest_command, check=True)
#         print("Pytest execution completed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error during pytest execution: {e}")
#
# def generate_allure_report():
#     """
#     Generate the Allure report from the results directory.
#     """
#     allure_generate_command = [
#         "allure",
#         "generate",
#         ALLURE_RESULTS_DIR,
#         "-o", "allure-report",
#         "--clean"
#     ]
#     try:
#         subprocess.run(allure_generate_command, check=True)
#         print("Allure report generated successfully.")
#     except subprocess.CalledProcessError as e:
#
#         print(f"Error during Allure report generation: {e}")
#
#
# run_pytest()
# generate_allure_report()
#
