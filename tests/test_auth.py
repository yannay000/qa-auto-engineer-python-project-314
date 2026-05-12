from selenium.webdriver.remote.webdriver import WebDriver

from config import LOGIN, PASSWORD
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from steps.login_steps import LoginSteps


def test_open_main_page(driver: WebDriver) -> None:
    page = LoginPage(driver)
    page.open()
    assert "Task manager" in driver.title


def test_login_success(driver: WebDriver) -> None:
    login_page = LoginPage(driver)
    header_page = HeaderPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)
    header_page.is_opened()


def test_logout_success(driver: WebDriver) -> None:
    login_steps = LoginSteps(driver)
    login_steps.login()

    login_steps.header_page.logout()
    assert login_steps.login_page.is_opened(
    ), "Login page is not opened after logout"

