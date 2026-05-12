from selenium.webdriver.common.by import By


class StatusCreateLocators:
    """Все селекторы страницы создания статуса"""

    NAME = (By.CSS_SELECTOR, '[name="name"]')
    SLUG = (By.CSS_SELECTOR, '[name="slug"]')
    SAVE = (By.CSS_SELECTOR, '[aria-label="Save"]')