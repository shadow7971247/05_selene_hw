import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_management():
    yield
    browser.quit()