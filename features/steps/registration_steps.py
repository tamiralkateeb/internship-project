

from behave import given, when, then
from app.application import Application

@given('the user is on the registration page')
def step_given_user_on_registration_page(context):
    context.app = Application(context.driver)
    context.app.open_page("https://soft.reelly.io/sign-up")

@when('the user enters "{text}" into the Full Name field')
def step_when_user_enters_full_name(context, text):
    context.app.registration_page.enter_full_name(text)  # Correct usage of registration_page

@when('the user enters "{text}" into the Phone Number field')
def step_when_user_enters_phone_number(context, text):
    context.app.registration_page.enter_phone(text)

@when('the user enters "{text}" into the Email field')
def step_when_user_enters_email(context, text):
    context.app.registration_page.enter_email(text)

@when('the user enters "{text}" into the Company Website field')
def step_when_user_enters_company_website(context, text):
    context.app.registration_page.enter_company_website(text)

@when('the user enters "{text}" into the Password field')
def step_when_user_enters_password(context, text):
    context.app.registration_page.enter_password(text)

@then('the entered information should be present in the respective fields')
def step_then_verify_entered_information(context):
    user_data = {
        "full_name": "ALEX",
        "phone": "+971 + test + careerist",
        "email": "ALEX@GMAIL.COM",
        "company_website": "test",
        "password": "USA3241"
    }
    context.app.registration_page.verify_input_values(user_data)
