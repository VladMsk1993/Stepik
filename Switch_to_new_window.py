from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):    # Функцию calc(), рассчитывает математичесую функцию от Х.
    return str(math.log(abs(12 * math.sin(int(x)))))    # Return возращает значения рассчитанной функции.


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element_by_class_name("btn-primary")
    button_1.click()

    #Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
    #Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0] #Сохраняем леременную с первой вкладкой, на случае, елси нужно с ней работать.
    window = browser.switch_to.window(new_window)    # Переключение на другую вкладку в браузере.


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