from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.CSS_SELECTOR, '[data-test="username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-test="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')

    def open_page(self):
        self.open(self.URL)

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
