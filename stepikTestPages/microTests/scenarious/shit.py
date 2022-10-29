import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class TestMainPage:

    @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",  "https://stepik.org/lesson/236899/step/1",  "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])


    def test_sending_answer(self, browser, links):
        link = f"{links}"
        browser.get(link)
        browser.implicitly_wait(3)
        browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area").send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button.click()  
        message = WebDriverWait(browser, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"div.smart-hints"))
        ).text
       
        assert(message=="Correct!")
        print(message)

