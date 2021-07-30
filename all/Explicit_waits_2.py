import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):    # Функцию calc(), рассчитывает математичесую функцию от Х.
    return str(math.log(abs(12 * math.sin(int(x)))))    # Return возращает значения рассчитанной функции.


try:

    browser = webdriver.Chrome()
    browser.get(link)
    # Ожидание в течении 12 сек, пока не появится текст 100 в поле с Id=price/
    get_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"),"100"))

    book = browser.find_element_by_id("book")
    book.click()

    get_number = browser.find_element_by_id("input_value")
    x = get_number.text
    y = calc(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

    alert = browser.switch_to.alert # Переключаемся на модальное окно.
    alert = alert.text  # Берём текст из модального окна
    print(alert)
    alert.accept() # Соглашаемся в модальном окне т.е. закрываем его.

finally:
    time.sleep(1)
    browser.quit()
