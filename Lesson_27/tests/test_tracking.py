import pytest
from Lesson_27.pages.tracking_page import TrackingPage


@pytest.mark.parametrize(
    "tracking_number, expected_status",
    [
        ("20451051785219", "Отримана"),  # Змініть очікуваний статус за потреби
    ],
)
def test_parcel_status(driver, tracking_number, expected_status):
    """Тест перевіряє, що статус посилки відповідає очікуваному."""
    tracking_page = TrackingPage(driver)
    tracking_page.open()

    tracking_page.enter_tracking_number(tracking_number)
    actual_status = tracking_page.get_parcel_status()

    assert actual_status == expected_status, f"Expected: {expected_status}, but got: {actual_status}"

