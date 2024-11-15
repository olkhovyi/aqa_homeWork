from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

# URL with authorization
url = f"https://{config.USERNAME}:{config.PASSWORD}@qauto2.forstudy.space"

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the page
    driver.get(url)
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    print("Authorization successful!")

    # XPath and CSS locators
    locators = [
        # XPath locators
        (By.XPATH, "//button[text()='Login']"),
        (By.XPATH, "//a[text()='Sign up']"),
        (By.XPATH, "//input[@placeholder='Email']"),
        (By.XPATH, "//input[@placeholder='Password']"),
        (By.XPATH, "//button[@id='submit']"),
        (By.XPATH, "//div[@class='header']//span[text()='QAuto']"),
        (By.XPATH, "//div[@class='form-group']//label[@for='email']"),
        (By.XPATH, "//div[contains(@class, 'input-container')]//input[@name='password']"),
        (By.XPATH, "//form[@id='login-form']//button[text()='Login']"),
        (By.XPATH, "//footer//a[@href='/terms']"),
        (By.XPATH, "//h1[contains(text(), 'Dashboard')]"),
        (By.XPATH, "//nav//ul/li/a[@href='/cars']"),
        (By.XPATH, "//div[@class='card']//h5[contains(text(), 'Car Info')]"),
        (By.XPATH, "//table[@id='car-table']//tr[1]/td[2]"),
        (By.XPATH, "//button[contains(text(), 'Add New Car')]"),
        (By.XPATH, "//div[contains(@class, 'modal-content')]//button[contains(text(), 'Save')]"),
        (By.XPATH, "//form[@id='add-car-form']//input[@name='brand']"),
        (By.XPATH, "//form[@id='add-car-form']//input[@name='model']"),
        (By.XPATH, "//form[@id='add-car-form']//input[@name='year']"),
        (By.XPATH, "//form[@id='add-car-form']//input[@name='price']"),
        (By.XPATH, "//div[@class='alert alert-success']"),
        (By.XPATH, "//span[contains(text(), 'Logout')]"),
        (By.XPATH, "//div[contains(@class, 'footer')]//p"),
        (By.XPATH, "//img[contains(@src, 'logo')]"),
        (By.XPATH, "//h2[contains(text(), 'Welcome to QAuto')]"),

        # CSS locators
        (By.CSS_SELECTOR, "button#login"),
        (By.CSS_SELECTOR, "a[href='/register']"),
        (By.CSS_SELECTOR, "input[placeholder='Email']"),
        (By.CSS_SELECTOR, "input[placeholder='Password']"),
        (By.CSS_SELECTOR, "button#submit"),
        (By.CSS_SELECTOR, "div.header span.logo"),
        (By.CSS_SELECTOR, "div.form-group label[for='email']"),
        (By.CSS_SELECTOR, "div.input-container input[name='password']"),
        (By.CSS_SELECTOR, "form#login-form button[type='submit']"),
        (By.CSS_SELECTOR, "footer a[href='/terms']"),
        (By.CSS_SELECTOR, "h1.dashboard-title"),
        (By.CSS_SELECTOR, "nav ul li a[href='/cars']"),
        (By.CSS_SELECTOR, "div.card h5.car-info"),
        (By.CSS_SELECTOR, "table#car-table tr:first-child td:nth-child(2)"),
        (By.CSS_SELECTOR, "button.add-car"),
        (By.CSS_SELECTOR, "div.modal-content button.save"),
        (By.CSS_SELECTOR, "form#add-car-form input[name='brand']"),
        (By.CSS_SELECTOR, "form#add-car-form input[name='model']"),
        (By.CSS_SELECTOR, "form#add-car-form input[name='year']"),
        (By.CSS_SELECTOR, "form#add-car-form input[name='price']"),
        (By.CSS_SELECTOR, "div.alert.alert-success"),
        (By.CSS_SELECTOR, "span.logout"),
        (By.CSS_SELECTOR, "div.footer p"),
        (By.CSS_SELECTOR, "img[src*='logo']"),
        (By.CSS_SELECTOR, "h2.welcome-message")
    ]

    # Verify all locators
    for by_type, selector in locators:
        try:
            element = wait.until(EC.presence_of_element_located((by_type, selector)))
            print(f"Element found: {selector}")
        except Exception as e:
            print(f"Element not found: {selector}. Error: {e}")

    # Interact with elements
    try:
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))

        email_input.send_keys(config.USERNAME)
        password_input.send_keys(config.PASSWORD)
        login_button.click()
        print("Login action performed!")

        # Verify successful login
        dashboard_header = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Dashboard')]")))
        print(f"Login successful, header found: {dashboard_header.text}")
    except Exception as e:
        print(f"Error during login interaction: {e}")

finally:
    driver.quit()
    print("Test completed!")
