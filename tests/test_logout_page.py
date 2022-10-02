from PageObject.logout_page_po import LogoutPage
import pytest


def test_check_logout(set_up_tear_down):
    page = set_up_tear_down
    login_page = LogoutPage(page)
    login_page.logout('standard_user', 'secret_sauce')

