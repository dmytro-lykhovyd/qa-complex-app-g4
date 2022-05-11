import logging
import random
import string
from time import sleep

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class User:
    log = logging.getLogger('[User]')

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(100000000000, 999999999999))

    @staticmethod
    def random_str(length=6):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    @pytest.fixture
    def registration_new_user(self):
        # Create Driver
        driver = WebDriver(executable_path="/Users/dmytrolykhovyd/PycharmProjects/Lykhovyd_project/chromedriver")

        # Open Start page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Start Page is opened')

        # Clear and fill Username field
        username = f"{self.random_str()}"
        username_field = driver.find_element(by=By.XPATH, value=".//input[@Placeholder='Pick a username']")
        username_field.clear()
        self.log.info('Username field is cleared')
        username_field.send_keys(username)
        self.log.info('Username field is filled')

        # Clear and fill Email field
        email = f"{self.random_str()}@random.mail"
        email_field = driver.find_element(by=By.XPATH, value=".//input[@Placeholder='you@example.com']")
        email_field.clear()
        self.log.info('Email field is cleared')
        email_field.send_keys(email)
        self.log.info('Email field is filled')

        # Clear and fill Password field
        password = f"{self.random_num()}"
        password_field = driver.find_element(by=By.XPATH, value=".//input[@Placeholder='Create a password']")
        password_field.clear()
        self.log.info('Password field is cleared')
        password_field.send_keys(password)
        sleep(3.0)
        self.log.info('Password field is filled')

        # Press 'Sign Up for OurApp' button
        signup_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        signup_button.click()
        sleep(3.0)
        self.log.info('Pressed Sign up button')

        credentials = [username, email, password]
        return credentials
