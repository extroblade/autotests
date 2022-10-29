from .base_page import BasePage
from .locators import LoginPageLocators

def go_to_cart(self):
    link = self.browser.find_element(*BasePageLocators.CART_LINK)
    link.click()