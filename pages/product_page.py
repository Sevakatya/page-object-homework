from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*BasketPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def check_message_after_adding_to_basket(self):
        basket_name = self.browser.find_element(*BasketPageLocators.MESSAGE_ADD_IN_BASKET).text
        product_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        assert basket_name == product_name, f"{basket_name} is not {product_name}"

    def check_price_after_adding_to_basket(self):
        price = self.browser.find_element(*BasketPageLocators.BASKET_PRICE).text.strip()
        check_product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
        assert check_product_price == price, f"{check_product_price} is not {price}"



