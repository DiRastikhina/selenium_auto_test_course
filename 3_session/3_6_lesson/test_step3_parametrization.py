import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    answer = math.log(int(time.time()))
    browser.get(link)
    browser.implicitly_wait(8)
    input1 = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
    input1.send_keys(answer)
    
    buttonS = browser.find_element(By.CSS_SELECTOR,".submit-submission")
    buttonS.click()
    
    browser.implicitly_wait(5)
    message = browser.find_element(By.CSS_SELECTOR,".smart-hints__hint")
    message_tx = message.text
    assert message_tx == "Correct!", f"Get {message_tx} instead Correct! message for {answer} in page {link}"
    