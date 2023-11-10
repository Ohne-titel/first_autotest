from selene import browser
import pytest


@pytest.fixture
def browser_configs():
    browser.config.window_width = 1024
    browser.config.window_height = 1366
    browser.open('https://google.com')
    yield
    browser.quit()
