import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """Фікстура для створення веб-драйвера."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Безголовий режим для швидшого виконання
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
