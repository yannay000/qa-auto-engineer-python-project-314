from selenium.webdriver.remote.webdriver import WebDriver

from pages.left_menu_page import LeftMenuPage
from pages.statuses_page import StatusesPage

class StatusesSteps:
    """Действия, доступные на для статусов"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open_statuses(self) -> None:
        left_menu_page = LeftMenuPage(self.driver)
        left_menu_page.open_statuses_page()
        self.statuses_page = StatusesPage(self.driver)
        assert self.statuses_page.is_opened(), "Statuses page is not opened"