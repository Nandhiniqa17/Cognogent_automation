from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from concurrent.futures import ThreadPoolExecutor
import time


# Function to automate user signup
def signup_user(user_number):
    try:
        # Setup WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Open the signup page
        driver.get("https://qa-frontend.cognogent.com")

        driver.find_element(By.XPATH,'//a[text()="Sign up"]').click()
        unique_email = f"user{user_number}_{int(time.time() * 1000)}@example.com"
        print(f"User {user_number}: {unique_email}")
        # Locate signup fields and enter details
        #driver.find_element(By.ID, "email").send_keys(f"user{user_number}")
        driver.find_element(By.ID, "email").send_keys(unique_email)
        driver.find_element(By.ID, "password").send_keys("Password123")
        #driver.find_element(By.ID, "confirm_password").send_keys("Password123")

        # Submit the signup form
        driver.find_element(By.XPATH, "//button[text()='Continue']").click()  # Replace with actual button locator

        # Optional: Verify successful signup
        time.sleep(3)  # Wait for response
        # success_message = driver.find_element(By.ID, "success_message").text
        # print(f"User {user_number}: {success_message}")

    except Exception as e:
        print(f"Error for User {user_number}: {e}")




# Main function to run 5 signups concurrently
if __name__ == "__main__":
    num_users = 5  # Number of concurrent users

    # Use ThreadPoolExecutor to run signups concurrently
    with ThreadPoolExecutor(max_workers=num_users) as executor:
        futures = [executor.submit(signup_user, i) for i in range(1, num_users + 1)]

        for future in futures:
            future.result()  # Wait for all threads to complete

    print(f"Signup test for {num_users} users completed. All {num_users} concurrent users completed.")
