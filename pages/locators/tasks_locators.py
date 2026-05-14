
from selenium.webdriver.common.by import By

from pages.locators.entities_locators import EntitiesLocators


class TasksLocators(EntitiesLocators):
    """Все селекторы страницы задачи"""

    CARDS_ROOT = (By.CLASS_NAME, 'MuiCard-root')
    ASSIGNEE_FILTER = (By.XPATH, "//input[@name='assignee_id']/preceding-sibling::div")
    STATUS_FILTER = (By.XPATH, "//input[@name='status_id']/preceding-sibling::div")
    LABEL_FILTER = (By.XPATH, "//input[@name='label_id']/preceding-sibling::div")
    CARD_ACTIONS = (By.CLASS_NAME, 'MuiCardActions-root')
    EDIT = (By.CSS_SELECTOR, '[aria-label="Edit"]')
    SHOW = (By.CSS_SELECTOR, '[aria-label="Show"]')
    ADD_FILTER = (By.CSS_SELECTOR, '[aria-label="Add filter"]')
    REMOVE_FILTERS = (By.XPATH, '//span[text()="Remove all filters"]')
    DRAFT_HEADER = (By.XPATH, '//h6[text()="Draft"]')
    FILTER_VALUES = (By.CSS_SELECTOR, '[role="option"]')
