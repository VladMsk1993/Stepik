from selenium import webdriver
from selenium.webdriver.common.by import By

Link = "http://suninjuly.github.io/simple_form_find_task.html"  # Переменная с сылкой.

try:
    browser = webdriver.Chrome()  # Открытие браузера
    browser.get(Link)  # Переход по ссылке
    button = browser.find_element(By.ID, "submit_button")  # Поиск селектора
    button.click()  # Нажатие на кнопку

finally:
    browser.quit()  # Закрытие браузера quit - закрывает браузер целиком в отличии от close, который закрывает только вкладку.

# Связка try\finally помогает в случае ошибки в первой части в любом случае закончить вторую.
