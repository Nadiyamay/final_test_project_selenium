from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        current_url = self.browser.current_url # реализуйте проверку на корректный url адрес
        assert  "login" in current_url, "URL does not include this word"

    def should_be_login_form(self):
        #login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert True, "Register form is not found"

    def register_new_user(self,email,password):
        email_register_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_INPUT)
        email_register_input.send_keys(email)
        password_register_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_INPUT)
        password_register_input.send_keys(password)
        password_repeat_register_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_REGISTER_INPUT)
        password_repeat_register_input.send_keys(password)
        submit_registration = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTER)
        submit_registration.click()