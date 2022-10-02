from PageObject.wrong_cred_login_page_po import WrongLoginPage


def test_wrong_auth_page(set_up_tear_down):
    page = set_up_tear_down
    wrong_login_page = WrongLoginPage(page)
    wrong_login_page.wrong_cred_login('standard_user', 'secret_sauc')