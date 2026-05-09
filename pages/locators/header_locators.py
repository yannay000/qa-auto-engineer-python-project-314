from selenium.webdriver.common.by import By


class HeaderLocators:

    WELCOME = (By.XPATH, '//span[text()="Welcome to the administration"]')
    PROFILE = (By.CSS_SELECTOR, '[aria-label="Profile"]')
    LOGOUT = (By.XPATH, '//span[text()="Logout"]')