from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL to the main page
url = "http://localhost:8000/dz.html"

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the main page
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Switch to first frame and verify
    driver.switch_to.frame("frame1")
    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")
    button1 = driver.find_element(By.TAG_NAME, "button")
    button1.click()
    time.sleep(1)
    alert1 = driver.switch_to.alert
    print(f"Frame1 alert: {alert1.text}")
    alert1.accept()

    # Switch back to main content
    driver.switch_to.default_content()

    # Switch to second frame and verify
    driver.switch_to.frame("frame2")
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")
    button2 = driver.find_element(By.TAG_NAME, "button")
    button2.click()
    time.sleep(1)
    alert2 = driver.switch_to.alert
    print(f"Frame2 alert: {alert2.text}")
    alert2.accept()

    # Success message
    print("Verification completed for both frames!")

finally:
    # Quit the browser
    driver.quit()
