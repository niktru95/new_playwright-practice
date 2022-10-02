from playwright.sync_api import expect


class WrongLoginPage:
    def __init__(self, page):
        self.page = page
        self.page.goto('https://www.saucedemo.com/')
        self.username = page.locator('//*[@id="user-name"]')
        self.password = page.locator('//*[@id="password"]')
        self.login_button = page.locator('//*[@id="login-button"]')
        self.message_error = page.locator('data-test=error')

    def wrong_cred_login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        expect(self.message_error).to_have_text('Epic sadface: Username and password do not match any user in this '
                                                'service')