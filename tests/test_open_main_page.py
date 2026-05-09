from config import url


def test_open_main_page(browser):
    browser.get(url)
    assert "Task manager" in browser.title