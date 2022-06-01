import random
import string

from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(100000000000, 999999999999))

    @staticmethod
    def random_str(length=6):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def fill_field(self, locator, value):
        """Send data into the field"""
        # Find field
        field = self.driver.find_element(by=By.XPATH, value=locator)
        # Clear field
        field.clear()
        # Fill field
        field.send_keys(value)

    def click_on_button(self, locator):
        """Find and Click on button"""
        self.driver.find_element(by=By.XPATH, value=locator).click()
