from selenium.webdriver.common.by import By

from pages.locators.entities_locators import EntitiesLocators


class LabelsLocators(EntitiesLocators):
    """Все селекторы страницы лейблов"""

    NAME_HEADER = (By.CSS_SELECTOR, '[data-field="name"]')
    NAME_COLUMN = (By.CLASS_NAME, 'column-name')