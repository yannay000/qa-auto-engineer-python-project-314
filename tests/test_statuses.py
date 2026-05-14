from selenium.webdriver.remote.webdriver import WebDriver

from pages.left_menu_page import LeftMenuPage
from pages.status_create_page import CreateStatusPage
from pages.statuses_page import StatusesPage
from steps.login_steps import LoginSteps
from steps.statuses_steps import StatusesSteps
from utils.data_generator import generate_status_params


def test_create_status(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    left_menu_page = LeftMenuPage(driver)
    left_menu_page.open_statuses_page()
    statuses_page = StatusesPage(driver)
    assert statuses_page.is_opened(), "Statuses page is not opened"

    statuses_page.open_create_status_page()
    status_create_page = CreateStatusPage(driver)
    assert status_create_page.is_opened(), "Status create page is not opened"

    test_status = generate_status_params()
    status_create_page.create_status(*test_status)

    left_menu_page.open_statuses_page()
    assert statuses_page.is_opened(), "Statuses page is not opened"
    statuses_page.status_exists(test_status[0])


def test_statuses_list(driver: WebDriver) -> None:

    login_steps = LoginSteps(driver)
    login_steps.login()

    statuses_steps = StatusesSteps(driver)
    statuses_steps.open_statuses()
    assert statuses_steps.statuses_page.get_statuses_count(
	) >= 5, "Not enough rows in statuses table"
    statuses_steps.statuses_page.table_headers_visible()


def test_edit_status(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    statuses_steps = StatusesSteps(driver)
    statuses_steps.open_statuses()
    status_params = statuses_steps.statuses_page.get_status_params_and_click()
    status_create_page = CreateStatusPage(driver)

    assert status_create_page.get_status_name_text() == status_params[
        0], "Incorrect status name"
    assert status_create_page.get_status_slug_text() == status_params[
        1], "Incorrect status slug"

    test_status = generate_status_params()
    status_create_page.edit_status(*test_status)

    left_menu_page = LeftMenuPage(driver)
    left_menu_page.open_statuses_page()
    assert statuses_steps.statuses_page.is_opened(), "Statuses page is not opened"
    statuses_steps.statuses_page.status_exists(test_status[0])


def test_delete_one_status(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    statuses_steps = StatusesSteps(driver)
    statuses_steps.open_statuses()

    statuses_count = statuses_steps.statuses_page.get_statuses_count()
    assert statuses_steps.statuses_page.delete_one_status() == statuses_count - 1, "Status wasn't deleted"


def test_delete_all_statuses(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    statuses_steps = StatusesSteps(driver)
    statuses_steps.open_statuses()

    assert statuses_steps.statuses_page.delete_all_statuses() == -1, "Not all statuses were deleted"
