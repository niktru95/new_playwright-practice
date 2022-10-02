from PageObject.cart_page_po import CartPage


def test_add_to_cart(set_up_tear_down):
    page = set_up_tear_down
    add_to_cart = CartPage(page)
    add_to_cart.login('standard_user', 'secret_sauce')
    add_to_cart.add_to_cart()
    add_to_cart.checkout_your_information()
    add_to_cart.checkout_overview()
    add_to_cart.checkout_complete()