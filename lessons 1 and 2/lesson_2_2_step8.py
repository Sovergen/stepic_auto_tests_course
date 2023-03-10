from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("имя")

    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"')
    input2.send_keys("фамилия")

    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("мыло")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson_2_2.txt')

    file1 = browser.find_element(By.CSS_SELECTOR, '#file')
    file1.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()