from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_tag_name("input")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_name("last_name")
    input_last_name.send_keys("Petrov")
    input_city = browser.find_element_by_class_name("city")
    input_city.send_keys("Moscow")
    input_country = browser.find_element_by_id("country")
    input_country.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()


