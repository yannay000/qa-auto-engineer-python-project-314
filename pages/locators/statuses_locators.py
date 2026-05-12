from selenium.webdriver.common.by import By

from pages.locators.entities_locators import EntitiesLocators


class StatusesLocators(EntitiesLocators):
    """Все селекторы страницы статусов"""

    NAME_HEADER = (By.CSS_SELECTOR, '[data-field="name"]')
    SLUG_HEADER = (By.CSS_SELECTOR, '[data-field="slug"]')
    NAME_COLUMN = (By.CLASS_NAME, 'column-name')
    SLUG_COLUMN = (By.CLASS_NAME, 'column-slug')
