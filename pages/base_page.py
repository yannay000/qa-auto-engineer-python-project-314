from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import IMPLEMENTATION


class BasePage:
    """Базовый класс со стандартными действиями"""
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def click(self, locator) -> None:
        """Ожидание кликабельности и клик"""
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def clear(self, locator) -> None:
        """Очистка формы ввода"""
        el = self.wait.until(EC.element_to_be_clickable(locator))
        # el.clear()
        command = Keys.CONTROL if IMPLEMENTATION else Keys.COMMAND
        el.send_keys(command, "a")   # на macOS вместо CONTROL используют Keys.COMMAND
        el.send_keys(Keys.DELETE)

    def type(self, locator, text: str) -> None:
        """Очистка и ввод текста"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def text_of(self, locator) -> str:
        """Получение текста элемента"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    def value_of(self, locator) -> str:
        """Получение текста элемента"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.get_attribute("value")

    def visible(self, loc):
        return self.wait.until(EC.visibility_of_element_located(loc))

    def find_elements(self, by_type, locator: str):
        return self.driver.find_elements(by_type, locator)
        # return self.wait.until(
        #     EC.presence_of_all_elements_located((by_type, locator))
        # )

    def find_element(self, parent, by_type, locator: str):
        return WebDriverWait(parent, 10).until(
            lambda p: p.find_element(by_type, locator)
        )
