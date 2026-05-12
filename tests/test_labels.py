from selenium.webdriver.remote.webdriver import WebDriver

from pages.label_create_page import CreateLabelPage
from pages.labels_page import LabelsPage
from pages.left_menu_page import LeftMenuPage
from steps.labels_steps import LabelsSteps
from steps.login_steps import LoginSteps
from utils.data_generator import generate_label_params


def test_create_label(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    left_menu_page = LeftMenuPage(driver)
    left_menu_page.open_labels_page()
    labels_page = LabelsPage(driver)
    assert labels_page.is_opened(), "Labels page is not opened"

    labels_page.open_create_label_page()
    label_create_page = CreateLabelPage(driver)
    assert label_create_page.is_opened(), "Label create page is not opened"

    test_label = generate_label_params()
    label_create_page.create_label(test_label)

    left_menu_page.open_labels_page()
    assert labels_page.is_opened(), "Labels page is not opened"
    labels_page.label_exists(test_label)


def test_labels_list(driver: WebDriver) -> None:

    login_steps = LoginSteps(driver)
    login_steps.login()

    labels_steps = LabelsSteps(driver)
    labels_steps.open_labels()
    assert labels_steps.labels_page.get_labels_count(
	) >= 5, "Not enough rows in labels table"
    labels_steps.labels_page.table_headers_visible()


def test_edit_label(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    labels_steps = LabelsSteps(driver)
    labels_steps.open_labels()
    label_params = labels_steps.labels_page.get_label_params_and_click()
    label_create_page = CreateLabelPage(driver)

    assert label_create_page.get_label_name_text() == label_params, "Incorrect label name"


def test_delete_one_label(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    labels_steps = LabelsSteps(driver)
    labels_steps.open_labels()

    labels_count = labels_steps.labels_page.get_labels_count()
    assert labels_steps.labels_page.delete_one_label() == labels_count - 1, "Label wasn't deleted"