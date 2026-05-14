from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    opts = Options()
    opts.add_argument("--window-size=1366,768")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--lang=ru-RU")
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox") # нужно в Docker
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--remote-allow-origins=*") 
    driver = webdriver.Chrome(options=opts)

    yield driver
    driver.quit()