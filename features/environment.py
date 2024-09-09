import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from app.application import Application


def browser_init(context, scenario_name=None):
    browser_type = os.getenv('BROWSER', 'chrome').lower()

    if os.getenv('USE_BROWSERSTACK'):
        BROWSERSTACK_USERNAME = os.getenv('BROWSERSTACK_USERNAME','tamiralkateeb_R3AjZD')
        BROWSERSTACK_ACCESS_KEY = os.getenv('BROWSERSTACK_ACCESS_KEY','CqXTKNqMkY25k7vdqWmy')

        url = f'http://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'

        options = ChromeOptions()
        bstack_options = {
            "os": "Windows",
            "osVersion": "10",
            "browserName": "Chrome",
            "sessionName": f"{scenario_name} - {context.feature.name}"
        }
        options.set_capability('bstack:options', bstack_options)

        context.driver = webdriver.Remote(command_executor=url, options=options)
    else:
        if browser_type == 'chrome':
            chrome_options = ChromeOptions()

            mobile_emulation = {"deviceName": "iPhone X"}
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_service = ChromeService(ChromeDriverManager().install())
            context.driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

        elif browser_type == 'firefox':
            firefox_options = FirefoxOptions()
            firefox_options.add_argument('headless')
            firefox_options.add_argument("--window-size=1920x1080")
            firefox_service = FirefoxService(GeckoDriverManager().install())
            context.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}. Please specify 'chrome' or 'firefox'.")

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print(f'\nStep failed: {step}')
        if hasattr(context, 'driver'):
            sanitized_step_name = re.sub(r'[^A-Za-z0-9]+', '_', step.name)
            screenshot_path = f"screenshots/{sanitized_step_name}.png"
            context.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()


def before_all(context):
    pass


def after_all(context):
    pass
