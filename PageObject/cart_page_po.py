from playwright.sync_api import expect


class CartPage:
    def __init__(self, page):
        self.page = page
        self.page.goto('https://www.saucedemo.com/')
        self.username = page.locator('//*[@id="user-name"]')
        self.password = page.locator('//*[@id="password"]')
        self.login_button = page.locator('//*[@id="login-button"]')
        self.title = page.locator('//*[@id="header_container"]/div[2]/span')
        self.add_to_crt = page.locator('//*[@id="add-to-cart-sauce-labs-backpack"]')
        self.shopping_cart_link = page.locator('//*[@id="shopping_cart_container"]/a')
        self.cart_title = page.locator('text=Your Cart')
        self.checkout = page.locator('data-test=checkout')
        self.first_name_field = page.locator('data-test=firstName')
        self.last_name_field = page.locator('data-test=lastName')
        self.post_code_field = page.locator('data-test=postalCode')
        self.continue_btn = page.locator('data-test=continue')
        self.title_product = page.locator('//*[@id="item_4_title_link"]/div')
        self.title_checkout_overview = page.locator('//*[@id="header_container"]/div[2]/span')
        self.total_price = page.locator('//*[@id="checkout_summary_container"]/div/div[2]/div[7]')
        self.finish_btn = page.locator('data-test=finish')
        self.thk_for_order_message = page.locator('//*[@id="checkout_complete_container"]/h2')
        self.message_error = page.locator('data-test=error')

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        expect(self.title).to_have_text('Products')

    def add_to_cart(self):
        self.add_to_crt.click()
        self.shopping_cart_link.click()
        expect(self.cart_title).to_have_text('Your Cart')
        self.checkout.click()

    def checkout_your_info_empty_fields(self):
        self.continue_btn.click()
        expect(self.message_error).to_have_text('Error: First Name is required')

    def checkout_your_information(self):
        self.first_name_field.fill('Nickolai')
        self.last_name_field.fill('Trushnikov')
        self.post_code_field.fill('183036')
        self.continue_btn.click()

    def checkout_overview(self):
        expect(self.title_checkout_overview).to_have_text('Checkout: Overview')
        expect(self.title_product).to_have_text('Sauce Labs Backpack')
        expect(self.total_price).to_have_text('Total: $32.39')
        self.finish_btn.click()

    def checkout_complete(self):
        expect(self.thk_for_order_message).to_have_text('THANK YOU FOR YOUR ORDER')