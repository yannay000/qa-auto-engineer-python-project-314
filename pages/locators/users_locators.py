from selenium.webdriver.common.by import By

from pages.locators.entities_locators import EntitiesLocators


class UsersLocators(EntitiesLocators):
    """Все селекторы страницы пользователей"""

    EMAIL_HEADER = (By.CSS_SELECTOR, '[data-field="email"]')
    FIRST_NAME_HEADER = (By.CSS_SELECTOR, '[data-field="firstName"]')
    LAST_NAME_HEADER = (By.CSS_SELECTOR, '[data-field="lastName"]')
    EMAIL_COLUMN = (By.CLASS_NAME, 'column-email')
    FIRST_NAME_COLUMN = (By.CLASS_NAME, 'column-firstName')
    LAST_NAME_COLUMN = (By.CLASS_NAME, 'column-lastName')
    NO_USERS = (By.XPATH, '//p[text()="No Users yet."]')
	