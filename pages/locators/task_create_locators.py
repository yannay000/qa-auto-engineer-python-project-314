from selenium.webdriver.common.by import By


class TaskCreateLocators:
    """Все селекторы страницы создания задачи"""

    ASSIGNEE = (By.XPATH, "//input[@name='assignee_id']/preceding-sibling::div")
    TITLE = (By.CSS_SELECTOR, '[name="title"]')
    STATUS = (By.XPATH, "//input[@name='status_id']/preceding-sibling::div")
