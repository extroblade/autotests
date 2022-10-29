from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
import math
import time
import pytest

login = str(time.time()) + "@fakemail.org"
password = str(time.time())


link_main = "https://selenium1py.pythonanywhere.com/"
link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class TestCartOffers():
    @pytest.mark.parametrize('id', ["0","1", "2", "3", "4", "5", "6", "8", "9"] )
    def test_check_cart_button(self, browser, id):
        link_offer = f"{link}?promo=offer{id}"
        page = ProductPage(browser, link_offer)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_equal_price()
        page.should_be_equal_name()


    @pytest.mark.xfail('expected error')
    @pytest.mark.parametrize('id', ["7"] )
    def test_check_cart_button_failed(self, browser, id):
        link_offer = f"{link}?promo=offer{id}"
        page = ProductPage(browser, link_offer)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_equal_price()
        page.should_be_equal_name()



class TestGuestScenarious():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_be_equal_price()
        page.should_be_equal_name()


    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link_main)
        page.open()
        page.go_to_cart()
        page.is_element_present(*ProductPageLocators.CART_NO_ITEMS)


    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_can_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_CART)


    def test_guest_cant_see_success_message_before_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_CART)#>>


class TestUsersScenarious():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(login, password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.is_element_present(*ProductPageLocators.PRODUCT_IN_CART)#>>
        

    def test_user_can_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_CART)#>>


    def test_user_cant_see_success_message_before_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_CART)#>>

