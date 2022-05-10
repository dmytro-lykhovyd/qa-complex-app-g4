import logging
import random
import string
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestRegistration:
    log = logging.getLogger('[Registration]')

    @staticmethod
    def random_str(length=2):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_username_warning_length_3(self):
        """
        1. Create driver
        2. Open start page
        3. Clear Username field
        4. Fill Username field with no more than 2 any characters
        5. Verify warning message
        """

        # Create driver
        driver = WebDriver(executable_path="/Users/dmytrolykhovyd/PycharmProjects/Lykhovyd_project/chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear Username field
        username_field = driver.find_element(by=By.XPATH, value=".//input[@Placeholder='Pick a username']")
        username_field.clear()
        self.log.info('Username field is cleared')

        # Fill Username field with no more than 2 any characters
        username = f"{self.random_str()}"
        username_field.send_keys(
            username)  # Оскільки реєстрація не відбувається, можемо юзати один набір даних для кожної ітерації, але най буде рандом
        self.log.info('Username field is filled with 2 characters')
        sleep(2.0)

        # Verify warning message
        warning_message = driver.find_element(by=By.XPATH,
                                              value=".//div[text()='Username must be at least 3 characters.']")
        assert warning_message.is_displayed(), 'Warning message is not displayed - test failed'
        self.log.info('Warning message is verified')

        driver.close()

    def test_username_warning_letters_numbers(self):
        """
        1.Create driver
        2.Open start page
        3.Clear Username field
        4.Fill Username field with no less than 3 spaces
        5.Verify warning message
        6.Clear Username field
        7.Fill Username field with no less than 3 noalpha nodigit characters
        8.Verify warning message
        """

        # Create driver
        driver = WebDriver(executable_path="/Users/dmytrolykhovyd/PycharmProjects/Lykhovyd_project/chromedriver")

        # Open start page
        self.log.info("Opening start page")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear Username field
        username_field = driver.find_element(by=By.XPATH, value=".//input[@Placeholder='Pick a username']")
        username_field.clear()
        self.log.info('Username field is cleared - step 1')

        username_field.send_keys(
            '   ')  # Оскільки реєстрація не відбувається, можемо юзати один набір даних для кожної ітерації. Чи це нормальний паттерн в такому випадку?
        self.log.info('Username field is filled with spaces')
        sleep(2.0)

        warning_message = driver.find_element(by=By.XPATH,
                                              value=".//div[text()='Username can only contain letters and numbers.']")
        assert warning_message.is_displayed(), 'Warning message is not displayed - test failed'
        self.log.info('Warning message is verified')

        username_field.clear()
        self.log.info('Username field is cleared - step 2')

        username_field.send_keys(
            '!@#$%^&*')  # Оскільки реєстрація не відбувається, можемо юзати один набір даних для кожної ітерації. Чи це нормальний паттерн в такому випадку?
        self.log.info('Username field is filled with noalpha nodogit characters')
        sleep(2.0)

        warning_message = driver.find_element(by=By.XPATH,
                                              value=".//div[text()='Username can only contain letters and numbers.']")
        assert warning_message.is_displayed(), 'Warning message is not displayed - test failed'
        self.log.info('Warning message is verified')

        driver.close()
