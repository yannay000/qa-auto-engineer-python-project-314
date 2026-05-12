from selenium.webdriver.remote.webdriver import WebDriver

from pages.left_menu_page import LeftMenuPage
from pages.users_page import UsersPage

class UsersSteps:
    """Действия, доступные на странице логина"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open_users(self) -> None:
        left_menu_page = LeftMenuPage(self.driver)
        left_menu_page.open_users_page()
        self.users_page = UsersPage(self.driver)
        assert self.users_page.is_opened(), "Users page is not opened"
