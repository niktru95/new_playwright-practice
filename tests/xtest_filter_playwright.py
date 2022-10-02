import pytest
from playwright.sync_api import Playwright
import allure

username_data = 'standard_user'
password_data = 'secret_sauce'


@pytest.mark.skip(reason='Не нужен')
@allure.feature('Test_filter')
def test_filter_find_and_add_to_cart(playwright: Playwright):
    # iphone = playwright.devices['iPhone XR']  #  создаем объект с параметрами запуска мобильных девайсов
    browser = playwright.chromium.launch()  # создаем браузер
    context = browser.new_context()  # создаем изолированный экземпляр браузера
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)  # начало записи действий в браузере
    page = context.new_page()  # создаем экземпляр закладки изолированного экземпляра браузера

    page.goto('https://www.saucedemo.com/')  # переходит на страницу

    page.locator('//*[@id="user-name"]').fill('standard_user')  # заполнение поля "username"

    page.locator('//*[@id="password"]').fill('secret_sauce')  # заполнение поля "password"

    page.locator('//*[@id="login-button"]').page.keyboard.press('Enter')  # имитирует нажатие клавиши "enter" на
    # кнопку "login"

    page.locator('data-test=product_sort_container').select_option("lohi")  # находит выпадающий список и кликает на
    # элемент в нем

    page.locator('text=Sauce Labs Onesie').click()  # кликает на заголовок товара

    page.locator('.shopping_cart_link').click()  # кликает на иконку корзины

    your_cart = page.locator('text=Your Cart')  # находит заголовок страницы корзины
    text_your_cart = your_cart.text_content()  # парсит содержимое заголовка страницы корзины

    assert text_your_cart == 'Your Cart'  # сравнивает спарсенное содержимое и ожидаемое значение

    page.locator('data-test=checkout').click()  # кликает на кнопку checkout

    page.locator('id=first-name').fill('Nick')  # заполняет поле "имя"
    page.locator('id=last-name').fill('Trushnikov')  # заполняет поле "фамилия"
    page.locator('id=postal-code').fill('183036')  # заполняет поле "почтовый индекс"

    page.locator('data-test=continue').click()  # кликает на кнопку "continue"

    checkout_overview = page.locator("text = Checkout: Overview")  # находит заголовок страницы проверки заказа
    get_checkout_overview = checkout_overview.text_content()  # парсит содержимое заголовка страницы проверки заказа

    assert get_checkout_overview == 'Checkout: Overview'  # сравнивает спарсенное содержимое и ожидаемое значение

    page.locator('data-test=finish').click()  # кликает на кнопку "finish"

    thank_for_order = page.locator('text = THANK YOU FOR YOUR ORDER')  # находит заголовок страницы завершения заказа
    get_thank_for_order = thank_for_order.text_content()  # парсит содержимое заголовка страницы завершения заказа

    assert get_thank_for_order == 'THANK YOU FOR YOUR ORDER'  # сравнивает спарсенное содержимое и ожидаемое значение

    # context.tracing.stop(path="trace.zip")  # конец записи действий в браузере

    context.close()  # закрывает контекст браузера
    browser.close()  # закрывает
