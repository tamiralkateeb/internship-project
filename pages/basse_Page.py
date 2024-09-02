from selenium import webdriver

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open_page(self, url: str):
        """Opens the browser."""
        self.driver.get(url)

    def find_element(self, locator: tuple):
        """Finds an element ."""
        return self.driver.find_element(*locator)

    def enter_text(self, locator: tuple, text: str):
        """Enters text into an input field."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_input_value(self, locator: tuple):
        """Gets the value from an input field."""
        return self.find_element(locator).get_attribute("value")
