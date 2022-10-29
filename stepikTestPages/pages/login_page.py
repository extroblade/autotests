from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_url(self):
        login_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
        assert True #add smth

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "no login form"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "no register form"


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_success_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM_SUCCESS), "Registration went wrong"


    def send_login_info(self, login):
        self.login_input = self.browser.find_element(*LoginPageLocators.LOGIN_NEW)
        self.login_input.send_keys(login)


    def send_password_info(self, password): 
        self.password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_NEW)
        self.password_input.send_keys(password)

        
    def send_password_repeat(self, password):
        self.password_input_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT)
        self.password_input_repeat.send_keys(password)

    
    def input_register_form(self, login, password):
        self.send_login_info(login)
        self.send_password_info(password)
        self.send_password_repeat(password)


    def register_new_user(self, login, password):
        self.should_be_login_page()
        self.input_register_form(login,password)
        self.button_register = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON).click()
        self.is_element_present(*LoginPageLocators.REGISTER_SUCCESS)
        self.should_be_success_form()
        self.should_be_authorized_user()
        
    
    
    





