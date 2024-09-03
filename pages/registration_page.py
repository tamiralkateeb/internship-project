# /pages/registration_page.py

from selenium.webdriver.common.by import By
from pages.basse_Page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.full_name_input = (By.CSS_SELECTOR, "#Full-Name")
        self.phone_input = (By.CSS_SELECTOR, "#phone2")
        self.email_input = (By.CSS_SELECTOR, "#Email-3")
        self.company_website_input = (By.CSS_SELECTOR, "#Company-website")
        self.password_input = (By.CSS_SELECTOR, "#field")

    def enter_full_name(self, full_name):
        self.enter_text(self.full_name_input, full_name)

    def enter_phone(self, phone):
        self.enter_text(self.phone_input, phone)

    def enter_email(self, email):
        self.enter_text(self.email_input, email)

    def enter_company_website(self, website):
        self.enter_text(self.company_website_input, website)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    def verify_input_values(self, user_data):
        assert self.get_input_value(self.full_name_input) == user_data["full_name"]
        assert self.get_input_value(self.phone_input) == user_data["phone"]
        assert self.get_input_value(self.email_input) == user_data["email"]
        assert self.get_input_value(self.company_website_input) == user_data["company_website"]
        assert self.get_input_value(self.password_input) == user_data["password"]
