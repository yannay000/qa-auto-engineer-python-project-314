from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.second_header_locators import SecondHeaderLocators
from pages.locators.task_create_locators import TaskCreateLocators


class CreateTaskPage(BasePage):

    def create_task(self, assignee: str, title: str, status: str) -> None:
        """Создание задачи"""
        self.click(TaskCreateLocators.ASSIGNEE)
        self.click((By.XPATH, f'//li[text()="{assignee}"]'))
        self.type(TaskCreateLocators.TITLE, title)
        self.click(TaskCreateLocators.STATUS)
        self.click((By.XPATH, f'//li[text()="{status}"]'))
        self.click(SecondHeaderLocators.SAVE)
        self.visible(SecondHeaderLocators.CREATED)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница создания задачи"""
        return self.driver.current_url.endswith("/tasks/create")

    def get_task_assignee_text(self) -> str:
        return self.value_of(TaskCreateLocators.ASSIGNEE)

    def get_task_title_text(self) -> str:
        return self.value_of(TaskCreateLocators.TITLE)

    def get_task_status_text(self) -> str:
        return self.value_of(TaskCreateLocators.STATUS)

    def edit_task(self, assignee: str, title: str, status: str) -> None:
        """Редактирование задачи"""
        self.click(TaskCreateLocators.ASSIGNEE)
        self.click((By.XPATH, f'//li[text()="{assignee}"]'))
        self.clear(TaskCreateLocators.TITLE)
        self.type(TaskCreateLocators.TITLE, title)
        self.click(TaskCreateLocators.STATUS)
        self.click((By.XPATH, f'//li[text()="{status}"]'))
        self.click(SecondHeaderLocators.SAVE)
        self.visible(SecondHeaderLocators.UPDATED)

    def edit_task_status(self, status: str = "Published") -> str:
        """Редактирование статуса задачи"""
        title = self.value_of(TaskCreateLocators.TITLE)
        self.click(TaskCreateLocators.STATUS)
        self.click((By.XPATH, f'//li[text()="{status}"]'))
        self.click(SecondHeaderLocators.SAVE)
        self.visible(SecondHeaderLocators.UPDATED)
        return title

    def delete_task(self) -> None:
        self.click(SecondHeaderLocators.DELETE)
