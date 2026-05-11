import os

from pages.base_page import BasePage
from pages.locators.login_locators import LoginLocators


class LoginPage(BasePage):
    URL = os.getenv("APP_BASE_URL")

    def open(self) -> None:
        """Открывает страницу логина"""
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """Авторизация"""
        self.type(LoginLocators.USERNAME, username)
        self.type(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.SUBMIT)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница авторизации"""
        return "/login" in self.driver.current_url
