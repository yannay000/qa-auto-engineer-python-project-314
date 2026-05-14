from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.second_header_locators import SecondHeaderLocators
from pages.locators.statuses_locators import StatusesLocators


class StatusesPage(BasePage):

    def open_create_status_page(self) -> None:
        self.click(SecondHeaderLocators.CREATE)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница пользователей"""
        self.visible(StatusesLocators.NAME_HEADER)
        return self.driver.current_url.endswith("/task_statuses")

    def status_exists(self, name: str):
        return self.visible((By.XPATH, f'//span[text()="{name}"]'))

    def get_statuses(self):
        return self.find_elements(*StatusesLocators.ENTITIES_TRS)

    def get_statuses_count(self) -> int:
        return len(self.get_statuses()) - 1

    def table_headers_visible(self):
        self.visible(StatusesLocators.NAME_HEADER)
        self.visible(StatusesLocators.SLUG_HEADER)

    def get_status_params_and_click(self, status_number: int = 1) -> tuple:
        status = self.get_statuses()[status_number]
        status_name = status.find_element(
            *StatusesLocators.NAME_COLUMN).find_element(*StatusesLocators.SPAN).text
        status_slug = status.find_element(
            *StatusesLocators.SLUG_COLUMN).find_element(
				*StatusesLocators.SPAN).text
        status.click()
        return status_name, status_slug

    def get_checkboxes(self):
        return self.find_elements(*StatusesLocators.CHECKBOXES)

    def delete_one_status(self, status_number: int = 1) -> int:
        self.get_checkboxes()[status_number].click()
        self.click(SecondHeaderLocators.DELETE)
        self.visible(SecondHeaderLocators.DELETED)
        return self.get_statuses_count()

    def delete_all_statuses(self) -> int:
        self.get_checkboxes()[0].click()
        self.click(SecondHeaderLocators.DELETE)
        return self.get_statuses_count()