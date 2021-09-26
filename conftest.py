from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(60)
    yield browser
    browser.quit()
