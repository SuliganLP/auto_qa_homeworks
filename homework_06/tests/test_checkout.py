from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_total(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open_page()
    login_page.login(username="standard_user", password="secret_sauce")

    products_page.add_backpack()
    products_page.add_bolt_tshirt()
    products_page.add_onesie()

    products_page.open_cart()
    cart_page.checkout()

    checkout_page.fill_checkout_form(first_name="Alexander", last_name="Test", postal_code="41068")

    checkout_page.continue_checkout()
    total = checkout_page.get_total()

    assert total == "$58.29"
