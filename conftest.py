import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver

    yield
    browser.quit()
