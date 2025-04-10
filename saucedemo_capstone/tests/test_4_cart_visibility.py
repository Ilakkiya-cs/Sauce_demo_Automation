"""
Tests visibility of the cart button after login.
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.driver_factory import DriverFactory


def test_cart_button_visibility():
    """
    Test if cart button is visible after logging in.
    """
    driver = DriverFactory.get_driver()
    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_element_visible(inventory_page.CART_ICON)
    finally:
        driver.quit()
