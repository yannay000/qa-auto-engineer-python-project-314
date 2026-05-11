from pages.left_menu_page import LeftMenuPage
from pages.user_create_page import CreateUserPage
from pages.users_page import UsersPage
from steps.login_steps import LoginSteps
from utils.generate_user import generate_user_params


def test_create_user(driver):
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




	



    