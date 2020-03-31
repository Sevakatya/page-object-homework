from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.base_page import BasePage
import pytest

link = "http://selenium1py.pythonanywhere.com"

def test_guest_can_go_to_login_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_should_be_empty()
    page.message_that_basket_is_empty_is_present()