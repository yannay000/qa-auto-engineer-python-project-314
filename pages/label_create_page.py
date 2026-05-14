from pages.base_page import BasePage
from pages.locators.label_create_locators import LabelCreateLocators
from pages.locators.second_header_locators import SecondHeaderLocators


class CreateLabelPage(BasePage):

    def create_label(self, name: str) -> None:
        """Создание лейбла"""
        self.type(LabelCreateLocators.NAME, name)
        self.click(SecondHeaderLocators.SAVE)
        self.visible(SecondHeaderLocators.CREATED)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница создания лейбла"""
        return self.driver.current_url.endswith("/labels/create")

    def get_label_name_text(self) -> str:
        return self.value_of(LabelCreateLocators.NAME)

    def edit_label(self, name: str) -> None:
        """Изменение лейбла"""
        self.clear(LabelCreateLocators.NAME)
        self.type(LabelCreateLocators.NAME, name)
        self.click(SecondHeaderLocators.SAVE)
        self.visible(SecondHeaderLocators.UPDATED)
