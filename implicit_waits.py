import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд, если элемент найден быстрей то, он запускается.
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    # Выводит асерт, если текст в поле не совпадает.
    assert "successful" in message.text
    message = message.text
    print(message)
finally:
    time.sleep(2)
    browser.quit()