import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.left_menu_page import LeftMenuPage
from pages.task_create_page import CreateTaskPage
from pages.tasks_page import TasksPage
from steps.login_steps import LoginSteps
from steps.tasks_steps import TasksSteps
from utils.data_generator import generate_task_params


def test_create_task(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    left_menu_page = LeftMenuPage(driver)
    left_menu_page.open_tasks_page()
    tasks_page = TasksPage(driver)
    assert tasks_page.is_opened(), "Tasks page is not opened"

    tasks_page.open_create_task_page()
    task_create_page = CreateTaskPage(driver)
    assert task_create_page.is_opened(), "Task create page is not opened"

    test_task = generate_task_params()
    test_task[0] = tasks_page.get_assignee_from_list()
    task_create_page.create_task(*test_task)

    left_menu_page.open_tasks_page()
    assert tasks_page.is_opened(), "Tasks page is not opened"
    tasks_page.task_exists(test_task[1])


def test_tasks_filter(driver: WebDriver) -> None:

    login_steps = LoginSteps(driver)
    login_steps.login()

    tasks_steps = TasksSteps(driver)
    tasks_steps.open_tasks()
    assert tasks_steps.tasks_page.get_tasks_count(
	) >= 15, "Not enough tasks on tasks page"

    tasks_steps.check_assignee_filter()

    tasks_steps.check_label_filter()

    tasks_steps.check_status_filter()


@pytest.mark.flaky
def test_edit_task_full(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    tasks_steps = TasksSteps(driver)
    tasks_steps.open_tasks()

    task = tasks_steps.tasks_page.get_tasks()[4]
    tasks_steps.tasks_page.edit_task(task)

    task_create_page = CreateTaskPage(driver)
    test_task = generate_task_params()
    test_task[0] = tasks_steps.tasks_page.get_assignee_from_list()
    task_create_page.edit_task(*test_task)

    left_menu_page = LeftMenuPage(driver)
    left_menu_page.open_tasks_page()
    assert tasks_steps.tasks_page.is_opened(), "Tasks page is not opened"
    tasks_steps.tasks_page.task_exists(test_task[1])


def test_edit_task_status(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    tasks_steps = TasksSteps(driver)
    tasks_steps.open_tasks()

    task = tasks_steps.tasks_page.get_tasks()[0]
    tasks_steps.tasks_page.edit_task(task)

    status = "Published"
    task_create_page = CreateTaskPage(driver)
    title = task_create_page.edit_task_status(status)

    left_menu_page = LeftMenuPage(driver)
    left_menu_page.open_tasks_page()
    assert tasks_steps.tasks_page.is_opened(), "Tasks page is not opened"
    task = tasks_steps.tasks_page.task_exists(title)
    assert tasks_steps.tasks_page.get_task_status(task) == status, "Task status not changed"


def test_delete_one_task(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    tasks_steps = TasksSteps(driver)
    tasks_steps.open_tasks()

    tasks_count = tasks_steps.tasks_page.get_tasks_count()
    tasks_steps.tasks_page.show_task(tasks_steps.tasks_page.get_tasks()[0])

    task_create_page = CreateTaskPage(driver)
    task_create_page.delete_task()

    left_menu_page = LeftMenuPage(driver)
    left_menu_page.open_tasks_page()
    assert tasks_steps.tasks_page.is_opened(), "Tasks page is not opened"
    assert tasks_steps.tasks_page.get_tasks_count() == tasks_count - 1, "Task wasn't deleted"
