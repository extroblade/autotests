from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage): 

    def add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button_add_to_cart.click()

    
    def should_be_products(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRODUCT_EXIST), "product"+\
            "is not presented"


    def should_be_equal_name(self):
        self.product_page_name = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_NAME).text

        self.product_cart_name = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located((ProductPageLocators.PRODUCT_CART_NAME))
        ).text
        
        assert self.product_cart_name == self.product_page_name, "Something went wrong ."+\
            ". Names are different"

    
    def should_be_equal_price(self):
        self.product_page_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_PRICE).text

        self.product_cart_price = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located((ProductPageLocators.PRODUCT_CART_PRICE))
        ).text
        
        assert self.product_page_price == self.product_cart_price, "Something went wrong ."+\
            ". Prices are different"



    def should_be_equal_data(self):
        assert True


    