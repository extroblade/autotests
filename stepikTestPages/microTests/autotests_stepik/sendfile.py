import time
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/file_input.html")



current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
fileSender = browser.find_element(By.CSS_SELECTOR, "#file")
fileSender.send_keys(file_path)

name = browser.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("a")
surname = browser.find_element(By.CSS_SELECTOR, "input:nth-child(4)").send_keys("b")
email = browser.find_element(By.CSS_SELECTOR, "input:nth-child(6)").send_keys("c@d.e")
#submitButton = browser.find_element(By.CSS_SELECTOR, "button").click()


time.sleep(10)
browser.quit() 