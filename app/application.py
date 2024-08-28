from pages.base_page import BasePage

class Application(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def register_user(self, user_data: dict):
        """Fills out the registration form with the provided user data."""
        self.enter_text(("css selector", "#Full-Name"), user_data["full_name"])
        self.enter_text(("css selector", "#phone2"), user_data["phone"])
        self.enter_text(("css selector", "#Email-3"), user_data["email"])
        self.enter_text(("css selector", "#Company-website"), user_data["company_website"])
        self.enter_text(("css selector", "#field"), user_data["password"])

    def verify_input_values(self, user_data: dict):
        """Verifies that the input values match the provided user data."""
        assert self.get_input_value(("css selector", "#Full-Name")) == user_data["full_name"]
        assert self.get_input_value(("css selector", "#phone2")) == user_data["phone"]
        assert self.get_input_value(("css selector", "#Email-3")) == user_data["email"]
        assert self.get_input_value(("css selector", "#Company-website")) == user_data["company_website"]
        assert self.get_input_value(("css selector", "#field")) == user_data["password"]
