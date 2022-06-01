from selene.api import *
from src.domain.user import User
from src.pages.LoginPage import LoginPage
from selene.api import browser

config.browser_name = "chrome"


def test_user_can_login():
    test_user = User("tomsmith", "SuperSecretPassword!")

    (LoginPage()
     .open()
     .login_as(test_user)
     .flash_message.should(have.text("You logged into a secure area!")))

    browser.quit()
