from selenium.webdriver.common.by import By


class StatusesLocators:
    """Все селекторы страницы статусов"""

    STATUSES_TRS = (By.CLASS_NAME, 'RaDatagrid-row')
    NAME_HEADER = (By.CSS_SELECTOR, '[data-field="name"]')
    SLUG_HEADER = (By.CSS_SELECTOR, '[data-field="slug"]')
    NAME_COLUMN = (By.CLASS_NAME, 'column-name')
    SLUG_COLUMN = (By.CLASS_NAME, 'column-slug')
    SPAN = (By.TAG_NAME, "span")
    CHECKBOXES = (By.CSS_SELECTOR, '[type="checkbox"]')