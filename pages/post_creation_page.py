from constants.post_creation_page import PostCreationPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class PostCreationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostCreationPageConstants()

    @log_wrapper
    def verify_sign_up_success(self):
        """Verify new user was sign-up successfully"""
        registration_confirm = self.wait_until_displayed(locator=self.constants.INVITATION_TEXT_XPATH)
        create_post_button = self.wait_until_displayed(locator=self.constants.CREATE_POST_BUTTON_XPATH)
        assert registration_confirm.text.__contains__(self.constants.INVITATION_TEXT_MESSAGE_PART), \
            'Registration failed'
        assert create_post_button.is_enabled(), 'Registration failed'

    @log_wrapper
    def log_out(self):
        self.click_on_button(locator=self.constants.SIGN_OUT_BUTTON_XPATH)
