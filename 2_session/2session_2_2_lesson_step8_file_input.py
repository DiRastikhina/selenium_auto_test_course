from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    name = browser.find_element(By.NAME, 'firstname')
    name.send_keys('Tom')
    
    lname = browser.find_element(By.NAME, 'lastname')
    lname.send_keys('Jerry')
    
    mail = browser.find_element(By.NAME, 'email')
    mail.send_keys('tom@jerry.org')
    
    file = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    file.send_keys(file_path)
    
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла