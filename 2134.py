import time

from selenium import webdriver


#Переход на страницу, поиск элементов
def init():
    driver.get("http://suninjuly.github.io/registration2.html")

    # Поля, обязательные для заполнения
    global first_name, last_name, email, phone, address, button, success
    first_name = driver.find_element_by_css_selector(".first_block .first")
    last_name = driver.find_element_by_css_selector(".first_block .second")
    email = driver.find_element_by_css_selector(".first_block .third")

    # Поля, необязатльные для заполнения
    phone = driver.find_element_by_css_selector(".second_block .first")
    address = driver.find_element_by_css_selector(".second_block .second")

    button = driver.find_element_by_css_selector("[type='submit']")

#Заполняем обязательные поля
def fill_required_fields():
    first_name.send_keys("Ivan")
    last_name.send_keys("Ivanov")
    email.send_keys("ivaivanov@mail.ru")
    button.click()

#Заполняем необязательные поля
def fill_optional_fields():
    phone.send_keys("+79999999999")
    address.send_keys("Ул.Пушкина,д.101.кв.52")
    button.click()



try:
    driver = webdriver.Chrome()
    init()
    fill_required_fields()



finally:
    time.sleep(3)
    driver.quit()

try:
    driver = webdriver.Chrome()
    init()
    fill_required_fields()
    fill_optional_fields()

finally:
    time.sleep(3)
    driver.quit()

try:
    driver = webdriver.Chrome()
    init()
    fill_optional_fields()

finally:
    time.sleep(3)
    driver.quit()