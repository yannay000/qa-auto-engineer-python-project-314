from selenium.webdriver.common.by import By


class UserCreatetLocators:
    """Все селекторы страницы создания пользователя"""

    EMAIL = (By.CSS_SELECTOR, '[name="email"]')
    FIRST_NAME = (By.CSS_SELECTOR, '[name="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, '[name="lastName"]')
    SAVE = (By.CSS_SELECTOR, '[aria-label="Save"]')