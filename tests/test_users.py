from selenium.webdriver.remote.webdriver import WebDriver

from pages.left_menu_page import LeftMenuPage
from pages.user_create_page import CreateUserPage
from pages.users_page import UsersPage
from steps.login_steps import LoginSteps
from steps.users_steps import UsersSteps
from utils.data_generator import generate_user_params


def test_create_user(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    left_menu_page = LeftMenuPage(driver)
    left_menu_page.open_users_page()
    users_page = UsersPage(driver)
    assert users_page.is_opened(), "Users page is not opened"

    users_page.open_create_user_page()
    user_create_page = CreateUserPage(driver)
    assert user_create_page.is_opened(), "User create page is not opened"

    test_user = generate_user_params()
    user_create_page.create_user(*test_user)

    left_menu_page.open_users_page()
    assert users_page.is_opened(), "Users page is not opened"
    users_page.user_exists(test_user[0])


def test_users_list(driver: WebDriver) -> None:

    login_steps = LoginSteps(driver)
    login_steps.login()

    users_steps = UsersSteps(driver)
    users_steps.open_users()
    assert users_steps.users_page.get_users_count(
	) >= 8, "Not enough rows in users table"
    users_steps.users_page.table_headers_visible()


def test_edit_user(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    users_steps = UsersSteps(driver)
    users_steps.open_users()
    user_params = users_steps.users_page.get_user_params_and_click()
    user_create_page = CreateUserPage(driver)

    assert user_create_page.get_user_email_text() == user_params[
        0], "Incorrect user text"
    assert user_create_page.get_user_first_name_text() == user_params[
        1], "Incorrect user first name"
    assert user_create_page.get_user_last_name_text() == user_params[
        2], "Incorrect user last name"

    user_create_page.validate_email()

    test_user = generate_user_params()
    user_create_page.edit_user(*test_user)

    left_menu_page = LeftMenuPage(driver)
    left_menu_page.open_users_page()
    assert users_steps.users_page.is_opened(), "Users page is not opened"
    users_steps.users_page.user_exists(test_user[0])


def test_delete_one_user(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    users_steps = UsersSteps(driver)
    users_steps.open_users()

    users_count = users_steps.users_page.get_users_count()
    assert users_steps.users_page.delete_one_user() == users_count - 1, "User wasn't deleted"


def test_delete_all_users(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    users_steps = UsersSteps(driver)
    users_steps.open_users()

    assert users_steps.users_page.delete_all_users() == -1, "Not all users were deleted"

