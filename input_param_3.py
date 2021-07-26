from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_name("firstname")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_name("lastname")
    input_last_name.send_keys("Petrov")
    input_mail = browser.find_element_by_name("e-mail")
    input_mail.send_keys("test@test.ru")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Неважное поле")
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


