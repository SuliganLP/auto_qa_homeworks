from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[data-test="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '[data-test="lastName"]')
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, '[data-test="postalCode"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-test="continue"]')
    TOTAL = (By.CSS_SELECTOR, '[data-test="total-label"]')

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

    def get_total(self):
        total_text = self.get_text(self.TOTAL)

        return total_text.replace("Total: ", "")
