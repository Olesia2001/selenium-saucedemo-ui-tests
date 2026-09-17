import os
import pytest

from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from pathlib import Path



@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    
    if os.getenv("CI") == "true":
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
    )

    options.add_argument(
        "--disable-features="
        "PasswordLeakDetection,"
        "PasswordManagerOnboarding"
    )

    browser = webdriver.Chrome(
        options=options
    )
    browser.maximize_window()

    yield browser

    browser.quit()

   
@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.open()
    login_page.login(
        'standard_user',
        'secret_sauce'
    )

    inventory_page.wait_until_opened()

    return driver 


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )



@pytest.fixture(autouse=True)

def screenshot_on_failure(request,driver):
    yield

    test_report = getattr(request.node,'rep-call',None)

    if test_report and test_report.failed:
        screenshots_directory = Path(
            'screenshots'
        )
        screenshots_directory.mkdir(
            exist_ok=True
        )

        screenshot_path = (
            screenshots_directory
            /f'{request.node.name}.png'
        )

        driver.save_screenshot(
            str(screenshot_path)
        )


