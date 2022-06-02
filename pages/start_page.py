from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def sign_in(self, username="", password=""):
        """Sign in user with credentials"""
        self.fill_field(locator=self.constants.SIGN_IN_USERNAME_XPATH, value=username)
        self.fill_field(locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.click_on_button(locator=self.constants.SIGN_IN_BUTTON_XPATH)

    def verify_sign_in_error(self):
        """Verify sign in error message"""
        error_message = self.driver.find_element(by=By.CSS_SELECTOR, value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT, 'Text is not valid'

    def sign_up(self, user):
        """Sign-up new user with randomized credentials"""
        self.fill_field(locator=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(locator=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(locator=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        sleep(2.0)
        self.click_on_button(locator=self.constants.SIGN_UP_BUTTON_XPATH)

    def verify_sign_up_success(self):
        """Verify new user was sign-up successfully"""
        registration_confirm = self.driver.find_element(by=By.XPATH, value=self.constants.INVITATION_TEXT_XPATH)
        create_post_button = self.driver.find_element(by=By.XPATH, value=self.constants.CREATE_POST_BUTTON_XPATH)
        assert registration_confirm.text.__contains__(self.constants.INVITATION_TEXT_MESSAGE_PART), \
            'Registration failed'
        assert create_post_button.is_enabled(), 'Registration failed'

    def verify_username_long_error(self, username=""):
        """Verify username long can not be shorter than 3 symbols"""
        self.fill_field(locator=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.click_on_button(locator=self.constants.SIGN_UP_BUTTON_XPATH)
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_UP_WARNING_MESSAGE_LENGTH_XPATH)
        assert error_message.text == self.constants.SIGN_UP_WARNING_MESSAGE_LENGTH_TEXT, 'Text is not valid'
        sleep(2.0)

    def verify_username_symbol_error(self, username=""):
        """Verify username can not contain special characters"""
        self.fill_field(locator=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.click_on_button(locator=self.constants.SIGN_UP_BUTTON_XPATH)
        error_message = self.driver.find_element(by=By.XPATH,
                                                 value=self.constants.SIGN_UP_WARNING_MESSAGE_CHARACTERS_XPATH)
        assert error_message.text == self.constants.SIGN_UP_WARNING_MESSAGE_CHARACTERS_TEXT, 'Text is not valid'

    def log_out(self):
        self.click_on_button(locator=self.constants.SIGN_OUT_BUTTON_XPATH)
