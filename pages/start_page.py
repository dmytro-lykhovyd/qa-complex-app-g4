from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.post_creation_page import PostCreationPage
from pages.utils import log_wrapper, wait_until_ok


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_wrapper
    def sign_in(self, username="", password=""):
        """Sign in user with credentials"""
        self.fill_field(locator=self.constants.SIGN_IN_USERNAME_XPATH, value=username)
        self.fill_field(locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.click_on_button(locator=self.constants.SIGN_IN_BUTTON_XPATH)
        return PostCreationPage(self.driver)

    @log_wrapper
    def verify_sign_in_error(self):
        """Verify sign in error message"""
        error_message = self.wait_until_displayed(locator=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT, 'Text is not valid'

    @log_wrapper
    def sign_up(self, user):
        """Sign-up new user with randomized credentials"""
        self.fill_field(locator=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(locator=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(locator=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        #  self.click_sign_up_verify()
        sleep(2)
        self.click_on_button(locator=self.constants.SIGN_UP_BUTTON_XPATH)
        return PostCreationPage(self.driver)

    @wait_until_ok(timeout=5, period=0.5)
    def click_sign_up_verify(self):
        """Click Sign Up and verify Sign Up button not exists"""
        self.click_on_button(locator=self.constants.SIGN_UP_BUTTON_XPATH)
        assert not self.is_element_exists(locator=self.constants.SIGN_UP_BUTTON_XPATH), 'Button still exists'

    @log_wrapper
    def verify_username_long_error(self, username=""):
        """Verify username long can not be shorter than 3 symbols"""
        self.fill_field(locator=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.click_on_button(locator=self.constants.SIGN_UP_BUTTON_XPATH)
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_UP_WARNING_MESSAGE_LENGTH_XPATH)
        assert error_message.text == self.constants.SIGN_UP_WARNING_MESSAGE_LENGTH_TEXT, 'Text is not valid'

    @log_wrapper
    def verify_username_symbol_error(self, username=""):
        """Verify username can not contain special characters"""
        self.fill_field(locator=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.click_on_button(locator=self.constants.SIGN_UP_BUTTON_XPATH)
        error_message = self.driver.find_element(by=By.XPATH,
                                                 value=self.constants.SIGN_UP_WARNING_MESSAGE_CHARACTERS_XPATH)
        assert error_message.text == self.constants.SIGN_UP_WARNING_MESSAGE_CHARACTERS_TEXT, 'Text is not valid'
