from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="checkout"]')

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
