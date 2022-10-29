import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/selects1.html")

num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
num = int(num1)+int(num2)
print(num)


selector = Select(browser.find_element(By.TAG_NAME, "select"))
selector.select_by_value(str(num))

submitButton = browser.find_element(By.CSS_SELECTOR, "button").click()
time.sleep(5)
browser.quit()