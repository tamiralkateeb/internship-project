import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def browser_init(context):
    """
    Initialize the browser for the test.
    :param context: Behave context
    """

    chrome_options = ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(
        options=chrome_options,
        service=chrome_service
    )

    firefox_options = FirefoxOptions()
    firefox_options.add_argument('headless')
    firefox_options.add_argument("--window-size=1920x1080")
    firefox_service = FirefoxService(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    print("Running in headless mode: ", "--headless" in chrome_options.arguments)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, scenario):
    context.driver.quit()

# features/environment.py

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(10)

def after_all(context):
    context.browser.quit()
