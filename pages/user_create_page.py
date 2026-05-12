from pages.base_page import BasePage
from pages.locators.second_header_locators import SecondHeaderLocators
from pages.locators.user_create_locators import UserCreateLocators


class CreateUserPage(BasePage):

    def create_user(self, email: str, first_name: str, last_name: str) -> None:
        """Создание пользователя"""
        self.type(UserCreateLocators.EMAIL, email)
        self.type(UserCreateLocators.FIRST_NAME, first_name)
        self.type(UserCreateLocators.LAST_NAME, last_name)
        self.click(SecondHeaderLocators.SAVE)
        self.visible(SecondHeaderLocators.CREATED)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница создания пользователя"""
        return self.driver.current_url.endswith("/users/create")

    def get_user_email_text(self) -> str:
        return self.value_of(UserCreateLocators.EMAIL)

    def get_user_first_name_text(self) -> str:
        return self.value_of(UserCreateLocators.FIRST_NAME)

    def get_user_last_name_text(self) -> str:
        return self.value_of(UserCreateLocators.LAST_NAME)
