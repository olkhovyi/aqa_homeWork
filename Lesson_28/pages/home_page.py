from selenium.webdriver.common.by import By

class HomePage:
    """Page Object for the main page"""
    def __init__(self, driver):
        self.driver = driver

    # Locator for the registration button
    SIGNUP_BUTTON = (By.CLASS_NAME, "hero-descriptor_btn")

    def get_signup_button(self):
        return self.driver.find_element(*self.SIGNUP_BUTTON)
