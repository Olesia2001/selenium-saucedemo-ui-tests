from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators import CheckoutPageLocators


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def click_continue(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable(
                CheckoutPageLocators.CONTINUE_BUTTON
            )
        )
        continue_button.click()

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(
                CheckoutPageLocators.ERROR_MESSAGE
            )
        )
        return error.text


    def fill_customer_information(self,
                                  first_name,
                                  last_name,
                                  postal_code):
        first_name_input = self.wait.until(
            EC.visibility_of_element_located(
                CheckoutPageLocators.FIRST_NAME_INPUT
            )
        )
        first_name_input.send_keys(first_name)

        last_name_input = self.wait.until(
            EC.visibility_of_element_located(
                CheckoutPageLocators.LAST_NAME_INPUT
            )
        )
        last_name_input.send_keys(last_name)

        postal_code_input = self.wait.until(
            EC.visibility_of_element_located(
                CheckoutPageLocators.POSTAL_CODE_INPUT
            )
        )
        postal_code_input.send_keys(postal_code)


    def click_finish(self):
        finish_button = self.wait.until(
            EC.visibility_of_element_located(
                CheckoutPageLocators.FINISH_BUTTON
            )
        )
        finish_button.click()

    def get_complete_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(
                CheckoutPageLocators.COMPLETE_MESSAGE
            )
        )
        return message.text

