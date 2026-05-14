from selenium.webdriver.remote.webdriver import WebDriver

from pages.labels_page import LabelsPage
from pages.left_menu_page import LeftMenuPage


class LabelsSteps:
    """Действия, доступные на для лейблов"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open_labels(self) -> None:
        left_menu_page = LeftMenuPage(self.driver)
        left_menu_page.open_labels_page()
        self.labels_page = LabelsPage(self.driver)
        assert self.labels_page.is_opened(), "Labels page is not opened"