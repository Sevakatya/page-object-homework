from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")

class RegisterPageLocators():
    REGISTER_FORM = (By.ID, "register_form")

class BasketPageLocators():
    BUTTON_ADD_TO_BASKET = (By.ID, "add_to_basket_form")
    MESSAGE_PRODUCT_ADDED_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info .alertinner p > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")