from selenium.webdriver.common.by import By


class EntitiesLocators:
    """Все селекторы страницы любой из сущностей"""

    ENTITIES_TRS = (By.CLASS_NAME, 'RaDatagrid-row')
    SPAN = (By.TAG_NAME, "span")
    CHECKBOXES = (By.CSS_SELECTOR, '[type="checkbox"]')