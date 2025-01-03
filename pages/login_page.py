from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//*[@name = 'username']")
    PASSWORD_INPUT = (By.XPATH, "//*[@name = 'password']")
    LOGIN_BUTTON = (By.LINK_TEXT, "Log in")
    USE_PASSKEY = (By.XPATH, "//*[text() = 'Use passkey']")

    def login(self, username, password):
        self.click(self.LOGIN_BUTTON)
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password + Keys.ENTER)
        self.click(self.USE_PASSKEY)
