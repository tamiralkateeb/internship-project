from pages.registration_page import RegistrationPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.registration_page = RegistrationPage(driver)

    def open_page(self, url):
        self.registration_page.open_page(url)

    def register_user(self, user_data: dict):
        """Fills out the registration form with the provided user data."""
        self.registration_page.enter_full_name(user_data["full_name"])
        self.registration_page.enter_phone(user_data["phone"])
        self.registration_page.enter_email(user_data["email"])
        self.registration_page.enter_company_website(user_data["company_website"])
        self.registration_page.enter_password(user_data["password"])

    def verify_input_values(self, user_data: dict):
        """Verifies that the input values match the provided user data."""
        self.registration_page.verify_input_values(user_data)
