from pages.base_page import BasePage
from pages.locators.second_header_locators import SecondHeaderLocators
from pages.locators.status_create_locators import StatusCreateLocators


class CreateStatusPage(BasePage):

    def create_status(self, name: str, slug: str) -> None:
        """Создание статуса"""
        self.type(StatusCreateLocators.NAME, name)
        self.type(StatusCreateLocators.SLUG, slug)
        self.click(StatusCreateLocators.SAVE)
        self.visible(SecondHeaderLocators.CREATED)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница создания статуса"""
        return self.driver.current_url.endswith("/task_statuses/create")

    def get_status_name_text(self) -> str:
        return self.value_of(StatusCreateLocators.NAME)

    def get_status_slug_text(self) -> str:
        return self.value_of(StatusCreateLocators.SLUG)