import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

@pytest.fixture(scope="session")
def driver():
    """Driver configuration fixture"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    """A fixture to initialize the main page's PageObject"""
    return HomePage(driver)

@pytest.fixture
def registration_page(driver):
    """A fixture for initializing the PageObject of the registration page"""
    return RegistrationPage(driver)

@pytest.fixture
def open_registration_page(home_page):
    """Fixture for opening the registration page"""
    signup_button = home_page.get_signup_button()
    signup_button.click()

@pytest.fixture
def fill_form(registration_page):
    """Fixture for filling out the registration form"""
    def _fill_form(name, last_name, email, password):
        registration_page.get_name_field().send_keys(name)
        registration_page.get_last_name_field().send_keys(last_name)
        registration_page.get_email_field().send_keys(email)
        registration_page.get_password_field().send_keys(password)
        registration_page.get_repeat_password_field().send_keys(password)
    return _fill_form

@pytest.fixture
def submit_form(registration_page):
    """Fixture for pressing the registration button"""
    def _submit():
        registration_page.get_register_button().click()
    return _submit

@pytest.fixture
def get_success_message(driver):
    """Fixture for receiving a message about successful registration"""
    def _get_message():
        try:
            success_alert = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
            )
            return success_alert.text
        except TimeoutException:
            return "A success message did not appear."
    return _get_message
