from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

import pytest 

pytestmark = pytest.mark.regression




def test_open_saucedemo(driver):
    login_page = LoginPage(driver)

    login_page.open()

    assert driver.title == 'Swag Labs'

@pytest.mark.smoke

def test_successful_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(
        'standard_user',
        'secret_sauce'
    )

    inventory_page.wait_until_opened()
   
    assert inventory_page.get_title() == 'Products'

@pytest.mark.parametrize(
    'username,password,expected_error',
    [
        ('standaed_user',
         'wrong_password',
         'Epic sadface: Username and password do not match any user in this service'),
        ('',
         'secret_sauce',
         'Epic sadface: Username is required'),
        ('standard_user',
         '',
         'Epic sadface: Password is required'),
        ('',
        '',
        'Epic sadface: Username is required'),
    ]
        
)
def test_unsuccessful_login(driver,
                            username,
                            password,
                            expected_error):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username,password)

    actual_error = login_page.error_message()

    assert actual_error == expected_error


def test_locked_out_user_cannot_login(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(
        'locked_out_user',
        'secret_sauce'
    )

    actual_error = login_page.error_message()

    assert actual_error == (
        'Epic sadface: Sorry, this user has been locked out.'
    )


def test_successful_logout(logged_in_driver):

    inventory_page = InventoryPage(logged_in_driver)
    login_page = LoginPage(logged_in_driver)

    inventory_page.logout()

    assert login_page.is_opened() is True



    






