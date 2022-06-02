from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    def wait_until_clickable(self, locator: str):
        """waits until element become clickable"""
        return self.waiter.until(method=expected_conditions.element_to_be_clickable((By.XPATH, locator)))

    def wait_until_displayed(self, locator: str):
        """waits until element become displayed"""
        return self.waiter.until(method=expected_conditions.visibility_of_element_located((By.XPATH, locator)))

    def is_element_exists(self, locator):
        """Check if certain element exists"""
        try:
            self.driver.find_elements(By=By.XPATH, value=locator)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

    def fill_field(self, locator: str, value: str):
        """Send data into the field"""
        field = self.wait_until_clickable(locator)
        field.clear()
        field.send_keys(value)

    def click_on_button(self, locator: str):
        """Find and Click on button"""
        self.wait_until_clickable(locator).click()
