from config import LOGIN, PASSWORD
from pages.header_page import HeaderPage
from pages.login_page import LoginPage


def test_open_main_page(browser):
    page = LoginPage(browser)
    page.open()
    assert "Task manager" in browser.title


def test_login_success(browser):
    login = LoginPage(browser)
    header = HeaderPage(browser)
    login .open()
    login.login(LOGIN, PASSWORD)
    header.is_opened()


def test_logout_success(browser):
    login = LoginPage(browser)
    header = HeaderPage(browser)
    login.open()
    login.login(LOGIN, PASSWORD)
    header.is_opened()

    header.logout()
    assert login.is_opened()

