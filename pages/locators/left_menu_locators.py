from selenium.webdriver.common.by import By


class LeftMenuLocators:
    """Все селекторы левого меню"""

    USERS = (By.CSS_SELECTOR, '[href="#/users"]')
    STATUSES = (By.CSS_SELECTOR, '[href="#/task_statuses"]')
    LABELS = (By.CSS_SELECTOR, '[href="#/labels"]')
