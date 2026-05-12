from selenium.webdriver.remote.webdriver import WebDriver

from config import LOGIN, PASSWORD
from pages.header_page import HeaderPage
from pages.login_page import LoginPage

class LoginSteps:
    """Действия, доступные на странице логина"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def login(self, login: str = LOGIN, password: str = PASSWORD) -> None:
        self.login_page = LoginPage(self.driver)
        self.header_page = HeaderPage(self.driver)
        self.login_page.open()
        self.login_page.login(LOGIN, PASSWORD)
        self.header_page.is_opened()

