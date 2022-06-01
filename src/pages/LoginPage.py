from selene.support.jquery_style_selectors import s
from selene.api import browser
from src.pages.HomePage import HomePage


class LoginPage(object):
    def __init__(self):
        self.email_input = s("#username")
        self.password_input = s("#password")
        self.login_button = s("#login > button")

    def open(self):
        browser.open_url("https://the-internet.herokuapp.com/login")
        return self

    def enter_email(self, email):
        self.email_input.set(email)
        return self

    def enter_password(self, password):
        self.password_input.set(password)
        return self

    def click_login_btn(self):
        self.login_button.click()
        return self

    def login_as(self, user):
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_login_btn()
        return HomePage()
