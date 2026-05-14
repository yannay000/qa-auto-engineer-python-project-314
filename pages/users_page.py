from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.second_header_locators import SecondHeaderLocators
from pages.locators.users_locators import UsersLocators


class UsersPage(BasePage):

    def open_create_user_page(self) -> None:
        self.click(SecondHeaderLocators.CREATE)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница пользователей"""
        self.visible(UsersLocators.EMAIL_HEADER)
        return self.driver.current_url.endswith("/users")

    def user_exists(self, email: str):
        return self.visible((By.XPATH, f'//span[text()="{email}"]'))

    def get_users(self):
        return self.find_elements(*UsersLocators.ENTITIES_TRS)

    def get_users_count(self) -> int:
        return len(self.get_users()) - 1

    def table_headers_visible(self):
        self.visible(UsersLocators.EMAIL_HEADER)
        self.visible(UsersLocators.FIRST_NAME_HEADER)
        self.visible(UsersLocators.LAST_NAME_HEADER)

    def get_user_params_and_click(self, user_number: int = 1) -> tuple:
        user = self.get_users()[user_number]
        user_email = user.find_element(
            *UsersLocators.EMAIL_COLUMN).find_element(*UsersLocators.SPAN).text
        user_first_name = user.find_element(
            *UsersLocators.FIRST_NAME_COLUMN).find_element(
				*UsersLocators.SPAN).text
        user_last_name = user.find_element(
            *UsersLocators.LAST_NAME_COLUMN).find_element(
				*UsersLocators.SPAN).text
        user.click()
        return user_email, user_first_name, user_last_name

    def get_checkboxes(self):
        return self.find_elements(*UsersLocators.CHECKBOXES)

    def delete_one_user(self, user_number: int = 1) -> int:
        self.get_checkboxes()[user_number].click()
        self.click(SecondHeaderLocators.DELETE)
        self.visible(SecondHeaderLocators.DELETED)
        return self.get_users_count()

    def delete_all_users(self) -> int:
        self.get_checkboxes()[0].click()
        self.click(SecondHeaderLocators.DELETE)
        return self.get_users_count()

