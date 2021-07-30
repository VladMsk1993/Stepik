import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
# Делаем параметризацию для того, чтобы запускать один и тот же тест под два условия. Также можно сделать для класса.
@pytest.mark.parametrize('language', ["ru", "en-gb"]) # Задаём параметр языка и вставляем необходимые языки.
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/" # Вызываем параметр.
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")