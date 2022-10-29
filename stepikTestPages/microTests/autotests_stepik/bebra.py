import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By 
browser = webdriver.Chrome()


browser.get("http://suninjuly.github.io/get_attribute.html")

valuex = browser.find_element(By.CSS_SELECTOR, "#treasure")
x = valuex.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

sendWindow = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

submitButton = browser.find_element(By.CSS_SELECTOR, "button").click()
time.sleep(5)
browser.quit()