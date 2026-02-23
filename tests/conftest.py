import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True)
def browser_management():
    # Путь к вашему chromedriver.exe
    service = Service(executable_path='C:/webdriver/chromedriver.exe')

    options = webdriver.ChromeOptions()

    # Указываем путь к созданному профилю
    options.add_argument('--user-data-dir=C:\\temp\\chrome_test_profile')

    # Дополнительные флаги для надёжности (можно оставить)
    options.add_argument('--disable-save-password-bubble')
    options.add_argument('--disable-notifications')
    options.add_argument('--start-maximized')

    # Убираем полоску "управляется автоматизированным ПО"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service=service, options=options)
    browser.config.driver = driver
    browser.config.timeout = 10

    yield
    browser.quit()