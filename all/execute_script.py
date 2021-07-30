import time
from selenium import webdriver
import math


link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):    # Функцию calc(), рассчитывает математичесую функцию от Х.
    return str(math.log(abs(12 * math.sin(int(x)))))    # Return возращает значения рассчитанной функции.


try:
    browser = webdriver.Chrome()
    browser.get(link)
    value_text = browser.find_element_by_id("input_value")   # Находим элемент.
    x = value_text.text   # Берём текс от найденного значения т.е. то что находиться между отк. и закрю тегами.
    value_of_x = calc(x)    # Запускаем математическую функцию от того значения, которе было найденно ранее.
    input_the_number = browser.find_element_by_id("answer")
    input_the_number.send_keys(value_of_x)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)   # Джава скрипт который запускается через
                                                                    # метода execute и прокручиватет страницу через скролл.
    checkbox = browser.find_element_by_css_selector(".form-check-custom .form-check-label")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()
    button.click()

finally:
    time.sleep(5)
    browser.quit()