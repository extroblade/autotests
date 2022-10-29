import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By 
browser = webdriver.Chrome()


browser.get("https://suninjuly.github.io/math.html")


x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)



answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)
robotButton = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
robotRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
submit = browser.find_element(By.CSS_SELECTOR, "button").click()
time.sleep(5)

browser.quit()