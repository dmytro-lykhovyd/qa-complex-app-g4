import logging

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


class TestStartPage:
    log = logging.getLogger('[StartPage]')

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(2)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

    @pytest.fixture(scope="function")
    def registered_user(self, start_page, random_user):
        post_creation_page = start_page.sign_up(random_user)
        post_creation_page.log_out()
        return random_user

    @pytest.fixture(scope="function")
    def signed_in_user(self, start_page, random_user):
        post_creation_page = start_page.sign_up(random_user)
        return post_creation_page, random_user

    def test_empty_fields_login(self, start_page):
        """
        - Preconditions:
            - Create Driver
            - Open Start page
        - Steps:
            - Clear field login
            - Clear field password
            - Click on 'Sign In' button
            - Verify error message
        """
        # Clear field Login
        # Clear field Password
        # Click on 'Sign In' button
        start_page.sign_in()

        # Verify error message
        start_page.verify_sign_in_error()

    def test_start_page_invalid_login(self, start_page, random_user):
        """
        - Preconditions:
            - Create Driver
            - Open Start page
        - Steps:
            - Clear Login field
            - Populate Login field with invalid data
            - Click on "Sign In" button
            - Verify error message
        """

        # Fill field Login
        # Fill field Password
        # Click on 'Sign In' button
        start_page.sign_in(username=random_user.username, password=random_user.password)

        # Verify error message
        start_page.verify_sign_in_error()

    def test_registration(self, start_page, random_user):
        """
        - Preconditions:
            - Create driver
            - Open start page
        - Steps:
            - Clear Username field
            - Fill Username field with 6 random symbols
            - Clear Email field
            - Fill e-mail field with valid format data
            - Clear Password field
            - Fill Password field with 12 random symbols
            - Press 'Sign Up for OurApp' button
            - Verify successful registration
        """

        # Fill Username, Email, Password
        # - sign up performing
        post_creation_page = start_page.sign_up(random_user)

        # - sign up success verifying
        post_creation_page.verify_sign_up_success()

    def test_username_warning_length_3(self, start_page, random_user):
        """
        - Preconditions:
            - Create driver
            - Open start page
        - Steps:
            - Clear Username field
            - Fill Username field with no more than 2 any characters
            - Verify warning message
        """

        start_page.verify_username_long_error(username=random_user.username[:2])

    def test_username_warning_letters_numbers(self, start_page):
        """
        - Preconditions:
            - Create driver
            - Open start page
        - Steps:
            - Fill Username field with no less than 3 spaces
            - Verify warning message
            - Clear Username field
            - Fill Username field with no less than 3 noalpha nodigit characters
            - Verify warning message
        """

        start_page.verify_username_symbol_error(username='!@#$%^&*()')

    def test_sign_in(self, start_page, registered_user):
        """
        - Preconditions:
            - Create driver
            - Open start page
            - Sign up new user
            - Log out
        - Steps:
            - Fill Username field with credentials previously generated
            - Fill Password field with credentials previously generated
            - Verify signing in
        """
        post_creation_page = start_page.sign_in(username=registered_user.username, password=registered_user.password)

        post_creation_page.verify_sign_up_success()

    def test_create_post(self, signed_in_user):
        """
        - Preconditions:
            - Create driver
            - Open start page
            - Sign up new user
        - Steps:
            - Press 'Create post' button
            - Fill Title field
            - Fill body field
            - Click 'Save new post' button
            - Verify new post was created
        """
        #  Go to fillable fields title, body

        post_creation_page, username = signed_in_user
        post_creation_page = post_creation_page.nav_to_create_post()

        #  Fill title and body
        post_creation_page.post_creation(title="qwerty", body="message")

        #  Verify message
        post_creation_page.verify_post_creation()
