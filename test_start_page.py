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
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

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
        self.log.info('Empty string user try to sign in')

        # Verify error message
        start_page.verify_sign_in_error()
        self.log.info('Error message is verified')

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
        self.log.info('User try to log in with invalid credentials')

        # Verify error message
        start_page.verify_sign_in_error()
        self.log.info('Error message is verified')

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
        start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
        self.log.info('User is registered')

        # - sign up success verifying
        start_page.verify_sign_up_success()
        self.log.info('Registration verified')

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
        self.log.info('Username field is filled with 2 random symbols')

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
        self.log.info('Username field is filled with special symbols')
