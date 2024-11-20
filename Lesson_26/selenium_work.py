from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# URL to the main page
url = "http://localhost:8000/dz.html"

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the main page
    driver.get(url)


    # Switch to first frame and verify
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))
    input1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input1")))
    input1.send_keys("Frame1_Secret")
    button1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    button1.click()

    # Wait for the alert, then get its text and accept it
    alert1 = WebDriverWait(driver, 10).until(EC.alert_is_present())
    print(f"Frame1 alert: {alert1.text}")
    alert1.accept()

    # Switch back to main content
    driver.switch_to.default_content()

    # Switch to second frame and verify
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2")))
    input2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input2")))
    input2.send_keys("Frame2_Secret")
    button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    button2.click()

    # Wait for the alert, then get its text and accept it
    alert2 = WebDriverWait(driver, 10).until(EC.alert_is_present())
    print(f"Frame2 alert: {alert2.text}")
    alert2.accept()

    # Success message
    print("Verification completed for both frames!")

finally:
    # Quit the browser
    driver.quit()
