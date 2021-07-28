import time, math, pytest
from selenium import webdriver


answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('qparam', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_input_time_into_area(browser, qparam):
    link = f"https://stepik.org/lesson/{qparam}/step/1//"
    browser.get(link)
    browser.implicitly_wait(3)
    input_param = browser.find_element_by_css_selector("#ember184")
    input_param.send_keys(answer)
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

