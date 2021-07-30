from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector(".first_block .first")
    first_name.send_keys("Ivancho")
    last_name = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    last_name.send_keys("Vitenko")
    email = browser.find_element_by_css_selector(".first_block .third")
    email.send_keys("Vitenko")
    time.sleep(2)
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()
    find_welcome_text = browser.find_element_by_tag_name("h1")
    welcome_text = find_welcome_text.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.quit()
