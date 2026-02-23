import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True)
def browser_management():
    service = Service(executable_path='C:/webdriver/chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\temp\\chrome_test_profile')
    options.add_argument('--disable-save-password-bubble')
    options.add_argument('--disable-notifications')
    options.add_argument('--start-maximized')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(service=service, options=options)
    browser.config.driver = driver
    browser.config.timeout = 10

    yield
    browser.quit()