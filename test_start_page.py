import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger('[StartPage]')

    def test_start_page(self):
        """
        - Create Driver
        - Open Start page
        - Clear field login
        - Clear field password
        - Click on 'Sign In' button
        - Verify error message
        """
        # Create Driver
        driver = WebDriver(executable_path="/Users/dmytrolykhovyd/PycharmProjects/Lykhovyd_project/chromedriver")

        # Open Start page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Start Page is opened')

        # Clear field Login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        self.log.info(login_field.get_attribute('placeholder'))
        login_field.clear()
        self.log.info('Login field is cleared')

        # Clear field Password

        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        self.log.info(password_field.get_attribute('placeholder'))
        password_field.clear()
        self.log.info('Password field is cleared')

        # Click on 'Sign In' button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info('Clicked on "Sign In" button')

        # Verify error message
        error_message = driver.find_element(by=By.CSS_SELECTOR,
                                            value="body > div.container.py-md-5 > div.alert.alert-danger.text-center")
        assert error_message.text == 'Error', 'Text is not valid'
        self.log.info('Error message is verified')

        # Close Driver
        driver.close()

    # Стоворити тест (поглядаючи на існуючий) який буде первіряти інвалід логін. Тобто заповнювати поля та первіряти помилку.

    def test_start_page_invalid_login(self):
        """
        1. Create Driver
        2. Open Start page
        3. Clear Login field
        4. Populate Login field with invalid data
        5. Click on "Sign In" button
        6. Verify error message
        """

        # Create Driver
        driver = WebDriver(executable_path="/Users/dmytrolykhovyd/PycharmProjects/Lykhovyd_project/chromedriver")
        self.log.info('Driver is created')

        # Open Start page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Start Page is opened')

        # Clear field Login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        self.log.info(login_field.get_attribute('placeholder'))
        login_field.clear()
        self.log.info('Login field is cleared')

        # Populate Login field with invalid login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.send_keys('12345')
        self.log.info('Login field is populated')

        # Click on 'Sign In' button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info('Clicked on "Sign In" button')

        # Verify error message
        error_message = driver.find_element(by=By.CSS_SELECTOR,
                                            value="body > div.container.py-md-5 > div.alert.alert-danger.text-center")
        assert error_message.text == 'Error', 'Text is not valid'
        self.log.info('Error message is verified')

        # Close Driver
        driver.close()
