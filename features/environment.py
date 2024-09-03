# /features/environment.py

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from app.application import Application

def browser_init(context, scenario_name):
    BROWSERSTACK_USERNAME = 'tamiralkateeb_R3AjZD'
    BROWSERSTACK_ACCESS_KEY = 'CqXTKNqMkY25k7vdqWmy'

    url = f'http://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'

    options = ChromeOptions()
    bstack_options = {
        "os": "Windows",
        "osVersion": "10",
        'browserName': 'Chrome',
        'sessionName': scenario_name


    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    browser_init(context, scenario.name)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
