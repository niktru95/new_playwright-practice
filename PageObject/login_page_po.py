from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.page.goto('https://www.saucedemo.com/')
        self.username = page.locator('//*[@id="user-name"]')
        self.password = page.locator('//*[@id="password"]')
        self.login_button = page.locator('//*[@id="login-button"]')
        self.title = page.locator('//*[@id="header_container"]/div[2]/span')

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        expect(self.title).to_have_text('Products')
