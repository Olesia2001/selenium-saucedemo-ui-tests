from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import Select

from pages.locators import InventoryPageLocators


class InventoryPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def wait_until_opened(self):
        self.wait.until(
            EC.url_contains('inventory.html')
        )

    def get_title(self):
        title = self.wait.until(
            EC.visibility_of_element_located(
                InventoryPageLocators.TITLE
            )
        )

        return title.text


    def get_product_count(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(
                InventoryPageLocators.PRODUCT_ITEMS
            )
        )
        return len(products)


    def get_product_names(self):
        product_elements = self.wait.until(
            EC.visibility_of_all_elements_located(
                InventoryPageLocators.PRODUCT_NAMES
            )
        )
        return [
            element.text
            for element in product_elements
        ]


    def add_backpack_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                InventoryPageLocators.ADD_BACKPACK_BUTTON
            )
        )
        button.click()


    def get_cart_items_count(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(
                InventoryPageLocators.CART_BADGE
            )
        )
        return int(badge.text)

    def open_cart(self):
        cart_link = self.wait.until(
            EC.element_to_be_clickable(
                InventoryPageLocators.CART_LINK
            )
        )
        cart_link.click()

    def sort_by_price_low_to_high(self):
        dropdown =self.wait.until(
            EC.element_to_be_clickable(
                InventoryPageLocators.SORT_DROPDOWN
            )
        )
        Select(dropdown).select_by_value('lohi')


    def get_product_prices(self):
        price_elements = self.wait.until(
            EC.visibility_of_all_elements_located(
                InventoryPageLocators.PRODUCT_PRICES
            )
        )
        return [
            float(element.text.replace('$', ''))
            for element in price_elements
        ]

    def add_bike_light_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                InventoryPageLocators.ADD_BIKE_LIGHT_BUTTON
            )
        )
        button.click()

    def logout(self):
        menu_button = self.wait.until(
            EC.element_to_be_clickable(
                InventoryPageLocators.MENU_BUTTON
            )
        )
        menu_button.click()

        logout_link = self.wait.until(
            EC.element_to_be_clickable(
                InventoryPageLocators.LOGOUT_LINK
            )
        )
        logout_link.click()




    
