from playwright.sync_api import Playwright
import pytest


@pytest.fixture(scope='function')
def set_up_tear_down(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    # page.set_viewport_size({'width': 1080, 'height': 1920})
    page.goto('https://www.saucedemo.com/')
    yield page
    context.close()
    browser.close()
