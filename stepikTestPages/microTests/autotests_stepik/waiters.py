import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
)
book = browser.find_element(By.CSS_SELECTOR, "#book").click()

x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
y = math.log(abs(12*math.sin(int(x))))

submitButton = browser.find_element(By.CSS_SELECTOR, "#solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton)
answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
submitButton.click()


alert = browser.switch_to.alert
print(alert.text.split(': ')[-1])
browser.quit()
