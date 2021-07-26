from selenium import webdriver
import time

link_1 = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link_1)
    time.sleep(1)

    search_link = browser.find_element_by_link_text("224592")
    search_link.click()

    input_first_name = browser.find_element_by_tag_name("input")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_name("last_name")
    input_last_name.send_keys("Petrov")
    input_city = browser.find_element_by_class_name("city")
    input_city.send_keys("Moscow")
    input_country = browser.find_element_by_id("country")
    input_country.send_keys("Russia")
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
