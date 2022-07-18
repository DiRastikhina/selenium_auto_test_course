import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  

def button_exists(self):
    try:
        self.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    except NoSuchElementException:
             return False
    return True
    

def test_check_add_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    
    assert button_exists(browser), "Seems i can't find the button to add in basket"
    
    