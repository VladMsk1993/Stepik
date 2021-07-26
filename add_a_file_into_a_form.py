from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    First_name = browser.find_element_by_name("firstname")
    First_name.send_keys("Viktor")
    Last_name = browser.find_element_by_name("lastname")
    Last_name.send_keys("Butenko")
    email = browser.find_element_by_name("email")
    email.send_keys("sdfsf@gmail.com")
    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # задаём путь к директории текущего исполняемого файла
                                                        # можно также указать адресс файла, если он находится не в папке со скриптом.
    file_path = os.path.join(current_dir, 'example.py')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
