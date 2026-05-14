import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.second_header_locators import SecondHeaderLocators
from pages.locators.tasks_locators import TasksLocators


class TasksPage(BasePage):

    def open_create_task_page(self) -> None:
        self.click(SecondHeaderLocators.CREATE)

    def is_opened(self) -> bool:
        """Проверяет, открыта ли страница задач"""
        self.visible(TasksLocators.DRAFT_HEADER)
        return self.driver.current_url.endswith("/tasks")

    def task_exists(self, title: str):
        return self.visible((By.XPATH, f'//div[text()="{title}"]')).find_element(
            *TasksLocators.PARENT).find_element(*TasksLocators.PARENT)

    def get_tasks(self):
        return self.find_elements(*TasksLocators.CARDS_ROOT)

    def get_tasks_count(self) -> int:
        return len(self.get_tasks())

    def show_task(self, task) -> None:
        task.find_element(*TasksLocators.CARD_ACTIONS).find_element(
			*TasksLocators.SHOW).click()
        self.visible(SecondHeaderLocators.SAVE)
        # self.find_element(task, *TasksLocators.CARD_ACTIONS).find_element(
        #     *TasksLocators.SHOW).click()

    def clear_filters(self) -> None:
        self.click(TasksLocators.ADD_FILTER)
        self.click(TasksLocators.REMOVE_FILTERS)

    def get_assignee_from_list(self, number: int = 3) -> str:
        self.click(TasksLocators.ASSIGNEE_FILTER)
        assignee = self.find_elements(*TasksLocators.FILTER_VALUES)
        return assignee[number].text

    def filter_by_assignee(self, assignee: str) -> int:
        # self.click(TasksLocators.ASSIGNEE_FILTER)
        self.click((By.XPATH, f'//li[text()="{assignee}"]'))
        for _i in range(10):
            tasks_count = self.get_tasks_count()
            if tasks_count < 15:
                return tasks_count
            time.sleep(1)
        return 0

    def filter_by_label(self, label: str) -> int:
        self.click(TasksLocators.LABEL_FILTER)
        self.click((By.XPATH, f'//li[text()="{label}"]'))
        for _i in range(10):
            tasks_count = self.get_tasks_count()
            if tasks_count < 15:
                return tasks_count
            time.sleep(1)
        return 0

    def get_task_status(self, task) -> str:
        return task.find_element(*TasksLocators.PARENT).find_element(
            *TasksLocators.PARENT).find_element(*TasksLocators.PRECEDING_SIBLING).text

    def filter_by_status(self, status: str):
        self.click(TasksLocators.STATUS_FILTER)
        self.click((By.XPATH, f'//li[text()="{status}"]'))
        for _i in range(10):
            tasks = self.get_tasks()
            if len(tasks) < 15:
                return tasks
            time.sleep(1)
        return

    def edit_task(self, task) -> None:
        task.find_element(*TasksLocators.CARD_ACTIONS).find_element(
            *TasksLocators.EDIT).click()
