from selenium.webdriver.common.by import By


class LoginLocators:
    """Все селекторы страницы логина"""

    USERNAME = (By.CSS_SELECTOR, '[name="username"]')
    PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    SUBMIT = (By.CSS_SELECTOR, '[type="submit"]')