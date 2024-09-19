from homework_10 import log_event


LOG_FILE = 'Lesson_10/login_system.log'


def test_log_success():
    # Call the function with success status
    log_event("test_user", "success")

    # We check the contents of the file
    with open(LOG_FILE, 'r') as log_file:
        log_content = log_file.read()

    assert "Login event - Username: test_user, Status: success" in log_content
    assert "INFO" in log_content  # We check that this is the info level

def test_log_expired():
    # Call the function with expired status
    log_event("test_user", "expired")

    # We check the contents of the file
    with open(LOG_FILE, 'r') as log_file:
        log_content = log_file.read()

    assert "Login event - Username: test_user, Status: expired" in log_content
    assert "WARNING" in log_content  # We check that this is a warning level

def test_log_failed():
    # Call the function with failed status
    log_event("test_user", "failed")

    # We check the contents of the file
    with open(LOG_FILE, 'r') as log_file:
        log_content = log_file.read()

    assert "Login event - Username: test_user, Status: failed" in log_content
    assert "ERROR" in log_content  # We check that this is an error level
