from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture(scope='session')
def browser_size():
    browser.open('https://google.com').driver.maximize_window()