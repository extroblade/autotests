import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/redirect_accept.html")

journ = browser.find_element(By.CSS_SELECTOR, "button").click()


new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
time.sleep(1)

x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
time.sleep(1)
answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(math.log((abs(12*math.sin(int(x))))))
submitButton = browser.find_element(By.CSS_SELECTOR, "button").click()

#time.sleep(10)
#browser.quit() 