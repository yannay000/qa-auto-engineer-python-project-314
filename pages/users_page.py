from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.second_header_locators import SecondHeaderLocators


class UsersPage(BasePage):

    def open_create_user_page(self) -> None:
        self.click(SecondHeaderLocators.CREATE)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница пользователей"""
        return self.driver.current_url.endswith("/users")

    def user_exists(self, email: str):
        return self.visible((By.XPATH, f'//span[text()="{email}"]'))
