from selenium.webdriver.common.by import By


class UsersLocators:
    """Все селекторы страницы пользователей"""

    USERS_TRS = (By.CLASS_NAME, 'RaDatagrid-row')
    EMAIL_HEADER = (By.CSS_SELECTOR, '[data-field="email"]')
    FIRST_NAME_HEADER = (By.CSS_SELECTOR, '[data-field="firstName"]')
    LAST_NAME_HEADER = (By.CSS_SELECTOR, '[data-field="lastName"]')
    EMAIL_COLUMN = (By.CLASS_NAME, 'column-email')
    FIRST_NAME_COLUMN = (By.CLASS_NAME, 'column-firstName')
    LAST_NAME_COLUMN = (By.CLASS_NAME, 'column-lastName')
    SPAN = (By.TAG_NAME, "span")
    CHECKBOXES = (By.CSS_SELECTOR, '[type="checkbox"]')
	