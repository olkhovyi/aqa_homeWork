import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

# Configuration
BASE_URL = "http://127.0.0.1:8080"
AUTH_ENDPOINT = "/auth"
CARS_ENDPOINT = "/cars"
USERNAME = "test_user"
PASSWORD = "test_pass"

# Logging configuration
LOG_FILENAME = "test_search.log"
logger = logging.getLogger("TestLogger")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(LOG_FILENAME, mode='w')  # Overwrites log file on each run
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)


# Fixture for authentication
@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    auth_response = session.post(
        f"{BASE_URL}{AUTH_ENDPOINT}",
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )
    if auth_response.status_code == 200:
        token = auth_response.json()["access_token"]
        session.headers.update({"Authorization": f"Bearer {token}"})
        logger.info("Authentication successful and session initialized.")
    else:
        logger.error("Authentication failed.")
        assert False, "Authentication failed"
    yield session
    session.close()


# Test parameters for search
@pytest.mark.parametrize("sort_by,limit", [
    ("price", 5),
    ("year", 10),
    ("engine_volume", 3),
    (None, 7),  # No sort_by, only limit
    ("brand", None),  # No limit, only sort_by
    ("nonexistent_field", 5),  # Invalid sort_by field
    (None, None),  # No parameters
])
def test_search_cars(auth_session, sort_by, limit):
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    response = auth_session.get(f"{BASE_URL}{CARS_ENDPOINT}", params=params)
    logger.info(f"GET request sent with params: {params}")
    assert response.status_code == 200, f"Failed request with params: {params}"

    cars = response.json()
    assert isinstance(cars, list), "Response is not a list"
    logger.info(f"Received {len(cars)} cars. Params: {params}")

    if sort_by:
        sorted_cars = sorted(cars, key=lambda x: x.get(sort_by, 0))
        assert cars == sorted_cars, f"Cars not sorted by {sort_by}"
        logger.info(f"Cars correctly sorted by {sort_by}")

    if limit:
        assert len(cars) <= limit, f"More cars returned than the limit {limit}"
        logger.info(f"Number of cars within the limit {limit}")
