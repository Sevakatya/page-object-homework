from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
     link = self.is_element_present(*MainPageLocators.LOGIN_LINK)
     link.click()
    # return LoginPage(browser=self.browser, url=self.browser.current_url)
    # При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес.
     alert = self.browser.switch_to.alert
     alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"