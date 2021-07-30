import time, math, pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()




@pytest.mark.parametrize('qparam', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_input_time_into_area(browser, qparam):
    link = f"https://stepik.org/lesson/{qparam}/step/1/"
    browser.get(link)
    browser.implicitly_wait(3)
    answer = math.log(int(time.time()))

    input_param = browser.find_element_by_css_selector(".ember-text-area.ember-view")
    input_param.send_keys(str(answer))

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    feed_back = browser.find_element_by_css_selector(".smart-hints__hint")
    feed_back = feed_back.text
    right_result = "Correct!"

    assert right_result == feed_back, f"Something is wrong. Expected '{right_result}' but we have '{feed_back}'"
    time.sleep(5)
