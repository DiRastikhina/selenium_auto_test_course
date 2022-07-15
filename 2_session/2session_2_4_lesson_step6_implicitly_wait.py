from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)
    
    browser.find_element(By.ID, "button")
    
finally:
    browser.quit()

# не забываем оставить пустую строку в конце файла