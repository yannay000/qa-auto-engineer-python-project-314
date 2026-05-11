from pages.base_page import BasePage
from pages.locators.second_header_locators import SecondHeaderLocators
from pages.locators.user_create_locators import UserCreatetLocators


class CreateUserPage(BasePage):

    def create_user(self, email: str, first_name: str, last_name: str) -> None:
        """Создание пользователя"""
        self.type(UserCreatetLocators.EMAIL, email)
        self.type(UserCreatetLocators.FIRST_NAME, first_name)
        self.type(UserCreatetLocators.LAST_NAME, last_name)
        self.click(UserCreatetLocators.SAVE)
        self.visible(SecondHeaderLocators.CREATED)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница пользователей"""
        return self.driver.current_url.endswith("/users/create")
