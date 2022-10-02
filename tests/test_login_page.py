from PageObject.login_page_po import LoginPage
import pytest



def test_check_login(set_up_tear_down):
    page = set_up_tear_down
    login_page = LoginPage(page)
    login_page.login('standard_user', 'secret_sauce')


