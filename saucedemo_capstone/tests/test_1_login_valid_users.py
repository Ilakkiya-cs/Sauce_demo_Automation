"""
Tests login with multiple valid users using data-driven approach and verifies session via cookies
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.driver_factory import DriverFactory
from utils.read_csv_data import get_login_data


@pytest.mark.parametrize("username,password", get_login_data("data/login_data.csv"))
def test_valid_login(username, password):
    """
    Test login for multiple valid users using data-driven approach.
    """
    if username == "locked_out_user":
        pytest.skip("locked_out_user is not allowed to login. Skipping test.")
    driver = DriverFactory.get_driver()
    try:
        login_page = LoginPage(driver)
        login_page.login(username, password)

        inventory_page = InventoryPage(driver)
        # Assert cart is visible (successful login indicator)
        assert inventory_page.is_element_visible(inventory_page.CART_ICON)

        # Validate session cookie instead of using URL/page-title
        cookie = driver.get_cookie("session-username")
        print("Session cookie:", cookie)

        assert cookie is not None
    finally:
        driver.quit()
