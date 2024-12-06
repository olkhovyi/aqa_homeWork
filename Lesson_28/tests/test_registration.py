def test_registration(driver, open_registration_page, fill_form, submit_form, get_success_message):
    """User registration verification test"""
    # Go to the registration page
    open_registration_page

    # Form filling
    fill_form(
        name="Mike",
        last_name="Jonson",
        email="mike_jonss1@example.com",
        password="Password1234"
    )

    # Form submission
    submit_form()

    # Checking the message about successful registration
    success_message = get_success_message()
    print(f"Message received after registration: {success_message}")

    if "registration complete" in success_message.lower():
        print("Registration completed successfully.")
    else:
        print(f"Unexpected message after registration: {success_message}")

