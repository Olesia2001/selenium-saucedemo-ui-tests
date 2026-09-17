from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (
        By.ID,
        "user-name"
    )

    PASSWORD_INPUT = (
        By.ID,
        "password"
    )

    LOGIN_BUTTON = (
        By.ID,
        "login-button"
    )
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )


    

class InventoryPageLocators:
    TITLE = (
        By.CSS_SELECTOR,
        ".title"
    )
    PRODUCT_ITEMS = (
        By.CSS_SELECTOR,
        '.inventory_item'
    )
    PRODUCT_NAMES = (
        By.CSS_SELECTOR,
        '.inventory_item_name'
    )
    ADD_BACKPACK_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    CART_BADGE = (
        By.CSS_SELECTOR,
        ".shopping_cart_badge"
    )

    CART_LINK = (
    By.CSS_SELECTOR,
    ".shopping_cart_link"
    )

    SORT_DROPDOWN = (
    By.CSS_SELECTOR,
    ".product_sort_container"
    )

    PRODUCT_PRICES = (
    By.CSS_SELECTOR,
    ".inventory_item_price"
    )

    ADD_BIKE_LIGHT_BUTTON = (
    By.ID,
    "add-to-cart-sauce-labs-bike-light"
    )
    MENU_BUTTON = (
    By.ID,
    "react-burger-menu-btn"
    )

    LOGOUT_LINK = (
    By.ID,
    "logout_sidebar_link"
    )

    
class CartPageLocators:
    ITEM_NAMES = (
        By.CSS_SELECTOR,
        ".inventory_item_name"
    )

    REMOVE_BACKPACK_BUTTON = (
    By.ID,
    "remove-sauce-labs-backpack"
    )

    CHECKOUT_BUTTON = (
    By.ID,
    "checkout"
    )

class CheckoutPageLocators:
    FIRST_NAME_INPUT = (
        By.ID,
        "first-name"
    )

    LAST_NAME_INPUT = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE_INPUT = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )
    FINISH_BUTTON = (
    By.ID,
    "finish"
    )

    COMPLETE_MESSAGE = (
    By.CSS_SELECTOR,
    ".complete-header"
    )







