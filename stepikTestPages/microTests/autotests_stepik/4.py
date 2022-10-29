import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/execute_script.html")


x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
y = math.log(abs(12*math.sin(int(x))))

sender = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
submitButton = browser.find_element(By.CSS_SELECTOR, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton)

toboter = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
ruler = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
submitButton.click()

time.sleep(10)
browser.quit()