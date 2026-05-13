
from pages.base_page import BasePage
from pages.locators.task_locators import TaskLocators


class TaskPage(BasePage):

    def get_task_assignee(self) -> str:
        return self.find_elements(*TaskLocators.ASSIGNEE_ROOT)[0].find_element(
            *TaskLocators.A).find_element(*TaskLocators.SPAN).text

    def get_task_label(self) -> str:
        return self.text_of(TaskLocators.LABEL)
