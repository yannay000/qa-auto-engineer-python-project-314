from selenium.webdriver.remote.webdriver import WebDriver

from pages.left_menu_page import LeftMenuPage
from pages.task_page import TaskPage
from pages.tasks_page import TasksPage


class TasksSteps:
    """Действия, доступные для задач"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open_tasks(self) -> None:
        self.left_menu_page = LeftMenuPage(self.driver)
        self.left_menu_page.open_tasks_page()
        self.tasks_page = TasksPage(self.driver)
        assert self.tasks_page.is_opened(), "Tasks page is not opened"

    def check_assignee_filter(self) -> None:
        assignee = self.tasks_page.get_assignee_from_list()
        self.task_page = TaskPage(self.driver)
        filtered_tasks_count = self.tasks_page.filter_by_assignee(assignee)
        for i in range(filtered_tasks_count):
            task = self.tasks_page.get_tasks()[i]
            self.tasks_page.show_task(task)
            assert self.task_page.get_task_assignee() == assignee, "Incorrect filtered task assignee"
            self.driver.back()
        self.tasks_page.clear_filters()

    def check_label_filter(self) -> None:
        label = "critical"
        self.task_page = TaskPage(self.driver)
        filtered_tasks_count = self.tasks_page.filter_by_label(label)
        assert filtered_tasks_count > 0, "Not enough tasks after filtering"
        for i in range(filtered_tasks_count):
            task = self.tasks_page.get_tasks()[i]
            self.tasks_page.show_task(task)
            assert self.task_page.get_task_label() == label, "Incorrect filtered task label"
            self.driver.back()
        self.tasks_page.clear_filters()

    def check_status_filter(self) -> None:
        status = "Published"
        self.task_page = TaskPage(self.driver)
        filtered_tasks = self.tasks_page.filter_by_status(status)
        assert filtered_tasks, "Not enough tasks after filtering"
        for task in filtered_tasks:
            assert self.tasks_page.get_task_status(task) == status, "Incorrect filtered task status"
        self.tasks_page.clear_filters()
