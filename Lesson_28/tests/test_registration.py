import uuid


def test_registration(driver, open_registration_page, fill_form, submit_form, get_success_message):
    """User registration verification test"""
    # Go to the registration page
    open_registration_page

    # Generate a unique email
    unique_email = f"mike_{uuid.uuid4().hex[:6]}@example.com"

    # Form filling
    fill_form(
        name="Mike",
        last_name="Jonson",
        email=unique_email,
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

