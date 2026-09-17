from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

import pytest


pytestmark = pytest.mark.regression

def test_backpack_is_added_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.wait_until_opened()

    item_names = cart_page.get_item_names()

    assert 'Sauce Labs Backpack' in item_names


def test_remove_backpack_from_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    cart_page = CartPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.wait_until_opened()


    cart_page.remove_backpack()

    assert cart_page.get_item_count() == 0

