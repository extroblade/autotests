import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class TestBucketPage:
    @pytest.mark.parametrize('links',["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/","http:vk.com/"])
    def test_bucket(self, browser, links):
        link = f"{links}"
        browser.get(link)
        browser.implicitly_wait(3)
        bucket = browser.find_element(By.CSS_SELECTOR, "a.btn.btn-default")
        assert(bucket)

