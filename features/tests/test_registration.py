import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_user_registration(browser):
    app = Application(browser)

    app.open_page("https://soft.reelly.io/sign-up")

    user_data = {
        "full_name": "ALEX",
        "phone": "+971 + test + careerist",
        "email": "ALEX@GMAIL.COM",
        "company_website": "test",
        "password": "USA3241"
    }

    app.register_user(user_data)

    app.verify_input_values(user_data)
