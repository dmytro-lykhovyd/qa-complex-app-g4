from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

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
