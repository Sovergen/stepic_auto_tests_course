from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

start_link = "https://suninjuly.github.io/selects2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(start_link)
    num1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = num1_element.text
    num2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = num2_element.text
    summ = int(num1)+int(num2)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(summ))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла