from selenium.webdriver.common.by import By


class TaskLocators:
    """Все селекторы страницы отображения одной задачи"""

    ASSIGNEE_ROOT = (By.CLASS_NAME, 'RaReferenceField-root')
    SPAN = (By.TAG_NAME, "span")
    A = (By.TAG_NAME, "a")
    LABEL = (By.CLASS_NAME, 'MuiChip-label')