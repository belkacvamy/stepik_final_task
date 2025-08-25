from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cururl=self.browser.current_url
        assert "login" in cururl, "Login is not found in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),"Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM),"Register form is not presented"

    def register_new_user(self,email,password):
        emailfield = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        passwordfield = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        passwordrepeatfield = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD)
        registersubmit=self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        emailfield.send_keys(email)
        passwordfield.send_keys(password)
        passwordrepeatfield.send_keys(password)
        registersubmit.click()