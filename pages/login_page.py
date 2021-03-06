from .base_page import BasePage
from .locators import LoginPageLocators, RegisterPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), "Register form is not found"

    def register_new_user(self, email, password):
        email_enter = self.browser.find_element(*RegisterPageLocators.EMAIL)
        password1 = self.browser.find_element(*RegisterPageLocators.PASSWORD1)
        password2 = self.browser.find_element(*RegisterPageLocators.PASSWORD2)
        email_enter.send_keys(email)
        password1.send_keys(password)
        password2.send_keys(password)
        button_submit = self.browser.find_element(*RegisterPageLocators.BUTTON_SUBMIT)
        button_submit.click()