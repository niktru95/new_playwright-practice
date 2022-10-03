from playwright.sync_api import Playwright
import pytest


@pytest.fixture()
def set_up_tear_down(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.saucedemo.com/')
    yield page
    context.close()
    browser.close()
