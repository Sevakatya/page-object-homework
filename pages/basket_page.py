from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "There should be no products in the basket"

    def message_that_basket_is_empty_is_present(self):
        expected_message = 'Your basket is empty.'
        message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert expected_message in message, "Text 'Your basket is empty.' should be present"
