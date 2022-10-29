import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


browser = webdriver.Chrome(options=options)
browser.maximize_window()


def functionTest():
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("a")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("a")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("a")
    browser.find_element(By.CSS_SELECTOR, ".second_block .first").send_keys("a")
    browser.find_element(By.CSS_SELECTOR, ".second_block .second").send_keys("a")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcomeText = browser.find_element(By.TAG_NAME, "h1").text
    welcomeTextExpected = "Congratulations! You have successfully registered!"
    assert welcomeTextExpected == welcomeText,"idc"


class TestAbs(unittest.TestCase):

    def test_reg1(self):
        
        browser.get(link1)
        functionTest()
        
        
    def test_reg2(self):
        
        browser.get(link2)
        functionTest()

browser.quit()

if __name__ == "__main__":
    unittest.main()

