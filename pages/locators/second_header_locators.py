from selenium.webdriver.common.by import By


class SecondHeaderLocators:
    """Все селекторы второго хедера"""

    CREATE = (By.CSS_SELECTOR, '[href="#/users/create"]')
    CREATED = (By.XPATH, '//div[text()="Element created"]')
    DELETE = (By.CSS_SELECTOR, '[aria-label="Delete"]')
    DELETED = (By.XPATH, '//div[text()="Element deleted"]')
