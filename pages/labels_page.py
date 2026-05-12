from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.labels_locators import LabelsLocators
from pages.locators.second_header_locators import SecondHeaderLocators


class LabelsPage(BasePage):

    def open_create_label_page(self) -> None:
        self.click(SecondHeaderLocators.CREATE)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница лейблов"""
        return self.driver.current_url.endswith("/labels")

    def label_exists(self, name: str):
        return self.visible((By.XPATH, f'//span[text()="{name}"]'))

    def get_labels(self):
        return self.find_elements(*LabelsLocators.ENTITIES_TRS)

    def get_labels_count(self) -> int:
        return len(self.get_labels()) - 1

    def table_headers_visible(self):
        self.visible(LabelsLocators.NAME_HEADER)

    def get_label_params_and_click(self, label_number: int = 1) -> str:
        label = self.get_labels()[label_number]
        label_name = label.find_element(
            *LabelsLocators.NAME_COLUMN).find_element(*LabelsLocators.SPAN).text
        label.click()
        return label_name

    def get_checkboxes(self):
        return self.find_elements(*LabelsLocators.CHECKBOXES)

    def delete_one_label(self, label_number: int = 1) -> int:
        self.get_checkboxes()[label_number].click()
        self.click(SecondHeaderLocators.DELETE)
        self.visible(SecondHeaderLocators.DELETED)
        return self.get_labels_count()