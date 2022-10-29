from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_NO_ITEMS = (By.CSS_SELECTOR, "#content_inner p")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    CART_PRODUCT_EXIST = (By.CSS_SELECTOR, "#basket_formset")
    CART_NO_ITEMS = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PAGE_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    PRODUCT_CART_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_CART_PRICE = (By.CSS_SELECTOR, "#messages p:nth-child(1) strong")
    PRODUCT_LINK = (By.CSS_SELECTOR, "#item_link")
    PRODUCT_IN_CART = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, "#messages div.alert.alert-safe.alert-noicon.alert-info.fade.in")
    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default[href]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_INPUT = (By.CSS_SELECTOR, "#login_link")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_NEW = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_NEW = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "#register_form button")
    REGISTER_SUCCESS = (By.CSS_SELECTOR, "alert-success")
    REGISTER_FORM_SUCCESS = (By.CSS_SELECTOR, "#messages div.alert.alert-success.fade.in")

