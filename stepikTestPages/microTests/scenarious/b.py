from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input").send_keys("a")
    browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input").send_keys("a")
    browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input").send_keys("a")
    browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.first_class > input").send_keys("a")
    browser.find_element(By.CSS_SELECTOR, "div.second_block > div.form-group.second_class > input").send_keys("a")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcomeText = browser.find_element(By.TAG_NAME, "h1").text
    welcomeTextExpected = "Congratulations! You have successfully registered!"
    assert welcomeTextExpected == welcomeText

finally:
    time.sleep(10)
    browser.quit()