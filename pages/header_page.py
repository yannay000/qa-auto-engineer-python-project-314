from pages.base_page import BasePage
from pages.locators.header_locators import HeaderLocators


class HeaderPage(BasePage):

    def logout(self):
        """Авторизация"""
        self.click(HeaderLocators.PROFILE)
        self.driver.fullscreen_window()
        self.click(HeaderLocators.LOGOUT)

    def is_opened(self):
        self.visible(HeaderLocators.WELCOME)
