from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
  
try: 
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button = browser.find_element(By.ID, "book")    
    button.click()
    
    browser.implicitly_wait(5)
    button2 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    
    x_element = browser.find_element(By.CSS_SELECTOR, '.form-group #input_value')
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID,'answer')
    input1.send_keys(y)
    
    
    button2.click()
    
    alert= browser.switch_to.alert
    print(alert.text)
    
finally:
  
    browser.quit()

# не забываем оставить пустую строку в конце файла