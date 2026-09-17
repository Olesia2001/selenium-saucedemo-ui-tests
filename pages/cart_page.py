from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators import CartPageLocators
from selenium.common.exceptions import StaleElementReferenceException


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            10,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

    
    def wait_until_opened(self):
        self.wait.until(
            EC.url_contains('cart.html')
        )

    def get_item_names(self):
        item_elements = self.wait.until(
            EC.visibility_of_all_elements_located(
                CartPageLocators.ITEM_NAMES
            )
        )
        return [
            element.text
            for element in item_elements
        ]

    def remove_backpack(self):
        remove_button = self.wait.until(
            EC.element_to_be_clickable(
                CartPageLocators.REMOVE_BACKPACK_BUTTON
            )
        )
        remove_button.click()

        self.wait.until(
            EC.staleness_of(remove_button)
        )


    def get_item_count(self):
        item_elements = self.driver.find_elements(
            *CartPageLocators.ITEM_NAMES
        )
        return len(item_elements)

    def click_checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(
                CartPageLocators.CHECKOUT_BUTTON
            )
        )
        checkout_button.click()

            


    
