import pytest
from pages.product_page import ProductPage
from pages.base_page import BasePage
import time

@pytest.mark.parametrize ('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.bookpage_add_to_basket
def test_guest_can_add_product_to_basket(browser, link):
    browser.get(link)
    product_page = ProductPage(browser, link)
    base_page = BasePage(browser, link)
    product_page.add_to_basket()
    base_page.solve_quiz_and_get_code()
    #time.sleep(10)
    product_page.check_message_after_adding_to_basket()
    product_page.check_price_after_adding_to_basket()




