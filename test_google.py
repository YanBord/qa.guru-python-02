from conftest import *

true_data = 'selene'
false_data = 'selinчд'
result = 'User-oriented Web UI browser tests in Python'


def test_first_positive(browser_size):
    browser.element('[name="q"]').should(be.blank).type(true_data).press_enter()
    browser.element('[id="search"]').should(have.text(result))


def test_second_negative(browser_size):
    browser.element('[name="q"]').should(be.blank).type(false_data).press_enter()
    browser.element('[id="search"]').should(have.no.text(result))
