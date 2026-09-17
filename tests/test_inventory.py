from pages.inventory_page import InventoryPage

import pytest
pytestmark = pytest.mark.regression

def test_inventory_contains_products(
        logged_in_driver
):
    inventory_page = InventoryPage(logged_in_driver)

    product_count = (inventory_page.get_product_count())

    assert product_count == 6


def test_inventory_contains_backpack(
        logged_in_driver
):
    inventory_page = InventoryPage(logged_in_driver)
    product_names = (
        inventory_page.get_product_names()
    )

    assert 'Sauce Labs Backpack' in product_names

@pytest.mark.smoke

def test_add_backpack_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()

    cart_items_count = (
        inventory_page.get_cart_items_count()
    )

    assert cart_items_count == 1


def test_sort_products_by_price_low_to_high(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.sort_by_price_low_to_high()

    actual_prices = (
        inventory_page.get_product_prices()
    )
    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices


def test_add_two_products_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    cart_items_count = (
        inventory_page.get_cart_items_count()
    )
    assert cart_items_count == 2 



