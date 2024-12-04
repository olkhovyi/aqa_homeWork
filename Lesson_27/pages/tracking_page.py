from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Lesson_27.pages.base_page import BasePage


class TrackingPage(BasePage):
    URL = "https://tracking.novaposhta.ua/#/uk"

    # Локатори
    INPUT_TRACKING_NUMBER = (By.CSS_SELECTOR, "input#en.track__form-group-input")
    STATUS_TEXT = (By.CSS_SELECTOR, ".header__status-text")

    def open(self):
        """Відкрити сторінку трекінгу."""
        self.open_url(self.URL)
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )  # Чекаємо завершення завантаження сторінки

    def enter_tracking_number(self, tracking_number):
        """Ввести номер накладної."""
        # Чекаємо завершення завантаження сторінки
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        # Знаходимо поле для вводу трек-номера
        input_field = self.wait_for_element(*self.INPUT_TRACKING_NUMBER)
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.RETURN)

    def get_parcel_status(self):
        """Отримати статус посилки."""
        status_element = self.wait_for_element(*self.STATUS_TEXT)
        return status_element.text
