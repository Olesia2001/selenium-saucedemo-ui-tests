from selenium.webdriver.support import (
    expected_conditions as EC
)
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators import LoginPageLocators



class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        username_input = self.wait.until(
            EC.visibility_of_element_located(
                LoginPageLocators.USERNAME_INPUT
            )
        )

        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait.until(
            EC.visibility_of_element_located(
                LoginPageLocators.PASSWORD_INPUT
            )
        )

        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                LoginPageLocators.LOGIN_BUTTON
            )
        )

        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(
                LoginPageLocators.ERROR_MESSAGE
            )
        )
        return error.text

    def is_opened(self):
        username_input = self.wait.until(
            EC.visibility_of_element_located(
                LoginPageLocators.USERNAME_INPUT
            )
        )
        return username_input.is_displayed()


