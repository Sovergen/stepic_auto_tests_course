from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest



class TestRegform(unittest.TestCase):
    def test_first_link(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block :nth-child(1) input')
        input1.send_keys("имя")

        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block :nth-child(2) input')
        input2.send_keys("фамилия")

        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block :nth-child(3) input')
        input3.send_keys("мыло")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        final = browser.find_element(By.CSS_SELECTOR, 'h1')
        self.assertEqual(final.text, "Congratulations! You have successfully registered!", "final frase is expected")
        
    def test_second_link(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block :nth-child(1) input')
        input1.send_keys("имя")

        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block :nth-child(2) input')
        input2.send_keys("фамилия")

        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block :nth-child(3) input')
        input3.send_keys("мыло")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        final = browser.find_element(By.CSS_SELECTOR, 'h1')
        self.assertEqual(final.text, "Congratulations! You have successfully registered!", "final frase is expected")
        
        
if __name__ == "__main__":
    unittest.main()