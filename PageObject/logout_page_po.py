from playwright.sync_api import expect


class LogoutPage:
    def __init__(self, page):
        self.page = page
        self.page.goto('https://www.saucedemo.com/')
        self.username = page.locator('//*[@id="user-name"]')
        self.password = page.locator('//*[@id="password"]')
        self.login_button = page.locator('//*[@id="login-button"]')
        self.burger_menu = page.locator('//*[@id="react-burger-menu-btn"]')
        self.sidebar_link = page.locator('//*[@id="logout_sidebar_link"]')
        self.login_button_after_logout = page.locator('//*[@id="login-button"]')

    def logout(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        self.burger_menu.click()
        self.sidebar_link.click()
        expect(self.login_button_after_logout).to_have_value('Login')
