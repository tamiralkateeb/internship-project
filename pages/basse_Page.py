# /pages/base_page.py

from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        """Opens the specified URL in the browser."""
        self.driver.get(url)

    def enter_text(self, locator, text):
        """Finds the element and enters the provided text."""
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_input_value(self, locator):
        """Gets the value from an input field."""
        return self.driver.find_element(*locator).get_attribute("value")
