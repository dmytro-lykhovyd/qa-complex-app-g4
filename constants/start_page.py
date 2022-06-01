class StartPageConstants:
    # Sign In
    SIGN_IN_USERNAME_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"

    # Sign In Error
    SIGN_IN_ERROR_MESSAGE_XPATH = "body > div.container.py-md-5 > div.alert.alert-danger.text-center"
    SIGN_IN_ERROR_MESSAGE_TEXT = "Invalid username / pasword"

    # Sign Up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@Placeholder='Pick a username']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@Placeholder='you@example.com']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@Placeholder='Create a password']"
    SIGN_UP_BUTTON_XPATH = ".//button[text()='Sign up for OurApp']"
    SIGN_UP_WARNING_MESSAGE_LENGTH_XPATH = ".//div[text()='Username must be at least 3 characters.']"
    SIGN_UP_WARNING_MESSAGE_LENGTH_TEXT = "Username must be at least 3 characters."
    SIGN_UP_WARNING_MESSAGE_CHARACTERS_XPATH = ".//div[text()='Username can only contain letters and numbers.']"
    SIGN_UP_WARNING_MESSAGE_CHARACTERS_TEXT = "Username can only contain letters and numbers."

    # Profile page
    INVITATION_TEXT_XPATH = ".//p[@class='lead text-muted']"
    INVITATION_TEXT_MESSAGE_PART = "Your feed displays"
    CREATE_POST_BUTTON_XPATH = ".//a[@class='btn btn-sm btn-success mr-2']"
