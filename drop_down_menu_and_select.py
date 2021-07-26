from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id("num1")
    number2 = browser.find_element_by_id("num2")
    x = number1.text   #Берём в виде текста значения в поле 1.
    y = number2.text   #Берём в виде текста значения в поле 2.
    sum_of_two = int(x) + int(y)   #Складывем два значения, переведя их из строки в число.
    some_value = sum_of_two

    select = Select(browser.find_element_by_css_selector(".custom-select"))   #Выбираем список через селект.
    select.select_by_value(str(some_value))   #Выбираем нужный элемент через метод селект, предворительно переводим его в строку.
    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    time.sleep(2)
    browser.quit()