from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):    # Функцию calc(), рассчитывает математичесую функцию от Х.
    return str(math.log(abs(12 * math.sin(int(x)))))    # Return возращает значения рассчитанной функции.


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element_by_class_name("btn-primary")
    button_1.click()

    alert = browser.switch_to.alert    # Переключение на модальное окно.
    alert.accept()   # Подтвереждение, также можно использовать dismiss для отказа.
    #Если нужно ввести какие-либо значения, тогда можно написать alert.sendkkeys().

    x = browser.find_element_by_id("input_value")
    x = x.text
    y = calc(x)

    input_value = browser.find_element_by_id("answer")
    input_value.send_keys(y)

    button_2 = browser.find_element_by_class_name("btn-primary")
    button_2.click()

finally:
    time.sleep(4)
    browser.quit()