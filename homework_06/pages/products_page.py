from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):
    BACKPACK_BUTTON = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    BOLT_TSHIRT_BUTTON = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    ONESIE_BUTTON = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-onesie"]')
    CART_BUTTON = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')

    def add_backpack(self):
        self.click(self.BACKPACK_BUTTON)

    def add_bolt_tshirt(self):
        self.click(self.BOLT_TSHIRT_BUTTON)

    def add_onesie(self):
        self.click(self.ONESIE_BUTTON)

    def open_cart(self):
        self.click(self.CART_BUTTON)
