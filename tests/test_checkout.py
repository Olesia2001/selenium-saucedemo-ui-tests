from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage

import pytest


pytestmark = pytest.mark.regression


def test_checkout_with_empty_fields(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()

    checkout_page.click_continue()

    assert (
        checkout_page.get_error_message()
        == "Error: First Name is required"
    )

@pytest.mark.smoke
def test_successful_checkout(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)
    checkout_page = CheckoutPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()

    checkout_page.fill_customer_information(
        first_name='Misha',
        last_name='tester',
        postal_code='443000'

    )
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert(
        checkout_page.get_complete_message()
        == "Thank you for your order!"
    )


