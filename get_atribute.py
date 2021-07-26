from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"


def calc(x): # Функцию calc(), рассчитывает и возвращает значение функции, которое нужно ввести в текстовое поле.
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    get_parameters = browser.find_element_by_id('treasure')
    valuex_par = get_parameters.get_attribute('valuex') #Берём атрибут (его значение).
    y = calc(valuex_par) # Запускаем функцию.

    find_answer = browser.find_element_by_id('answer')
    find_answer.send_keys(y)
    find_checkbox = browser.find_element_by_id("robotCheckbox")
    find_checkbox.click()
    find_radiobutton = browser.find_element_by_id("robotsRule")
    find_radiobutton.click()
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
