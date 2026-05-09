from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Базовый класс со стандартными действиями"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        """Ожидание кликабельности и клик"""
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def type(self, locator, text):
        """Очистка и ввод текста"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def text_of(self, locator):
        """Получение текста элемента"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    def text(self, loc):
        return self.wait.until(EC.visibility_of_element_located(loc)).text

    def visible(self, loc):
        return self.wait.until(EC.visibility_of_element_located(loc))