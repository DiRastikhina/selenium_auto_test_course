from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    
    first_window = browser.window_handles[0] # наша первая страница на память
    new_window = browser.window_handles[1] # новая открывшаяся вкладка
    browser.switch_to.window(new_window) # переключение на новую вкладку
    
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID,'answer')
    input1.send_keys(y)
    
    button2 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button2.click()
    
    alert= browser.switch_to.alert
    print(alert.text)
    
finally:
    # успеваем скопировать код за 30 секунд
    #time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла