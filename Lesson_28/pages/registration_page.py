from selenium.webdriver.common.by import By

class RegistrationPage:
    """Page Object for the registration page"""
    def __init__(self, driver):
        self.driver = driver

    # Registration form locators
    NAME_FIELD = (By.ID, "signupName")
    LAST_NAME_FIELD = (By.ID, "signupLastName")
    EMAIL_FIELD = (By.ID, "signupEmail")
    PASSWORD_FIELD = (By.ID, "signupPassword")
    REPEAT_PASSWORD_FIELD = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".modal-footer .btn-primary")

    def get_name_field(self):
        return self.driver.find_element(*self.NAME_FIELD)

    def get_last_name_field(self):
        return self.driver.find_element(*self.LAST_NAME_FIELD)

    def get_email_field(self):
        return self.driver.find_element(*self.EMAIL_FIELD)

    def get_password_field(self):
        return self.driver.find_element(*self.PASSWORD_FIELD)

    def get_repeat_password_field(self):
        return self.driver.find_element(*self.REPEAT_PASSWORD_FIELD)

    def get_register_button(self):
        return self.driver.find_element(*self.REGISTER_BUTTON)
