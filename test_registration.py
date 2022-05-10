import logging
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestRegistration:
    log = logging.getLogger('[Registration]')

    def test_registration(self):
        """
        1. Create driver
        2. Open start page
        3. Clear Username field
        4. Clear Email field
        5. Clear Password field
        6. Fill Username field with 3 random symbols
        7. Fill e-mail field with valid format data
        8. Fill Password field with 12 random symbols
        9. Press 'Sign Up for OurApp' button
        10. Verify successful registration
        """

        # Create Driver
        driver = WebDriver(executable_path="/Users/dmytrolykhovyd/PycharmProjects/Lykhovyd_project/chromedriver")

        # Open Start page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Start Page is opened')

        # Clear Username field
        username_field = driver.find_element(by=By.XPATH, value=".//input[@Placeholder='Pick a username']")
        username_field.clear()
        self.log.info('Username field is cleared')

        # Clear Email field
        email_field = driver.find_element(by=By.XPATH, value=".//input[@Placeholder='you@example.com']")
        email_field.clear()
        self.log.info('Email field is cleared')

        # Clear Password field
        password_field = driver.find_element(by=By.XPATH, value=".//input[@Placeholder='Create a password']")
        password_field.clear()
        self.log.info('Password field is cleared')

        # Fill Username field
        try:
            username_field.send_keys('RandomName125')
            self.log.info('Username field is filled')
        except Exception:
            driver.close()
            self.log.info('That username is already taken')

        # Fill Email field
        email_field.send_keys('random125@random.com')
        self.log.info('Email field is filled')

        # Fill Password field
        password_field.send_keys('123456123456')
        sleep(3.0)
        self.log.info('Password field is filled')

        # Press 'Sign Up for OurApp' button
        signup_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        signup_button.click()
        sleep(3.0)
        self.log.info('Pressed Sign up button')

        # Verify successful registration
        registration_confirm = driver.find_element(by=By.XPATH, value=".//p[@class='lead text-muted']")
        assert registration_confirm.text.__contains__('Your feed displays'), 'Registration failed'
        self.log.info('Registration verified')

        # Close Driver
        driver.close()
