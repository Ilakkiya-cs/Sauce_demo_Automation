"""
Verifies visibility and functionality of the logout button.
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.driver_factory import DriverFactory


def test_logout_button_functionality():
    """
    Test if logout button is visible and functions correctly.
    """
    driver = DriverFactory.get_driver()
    try:
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Step 2: Open menu and logout button is visible
        inventory_page = InventoryPage(driver)
        inventory_page.open_logout_menu()

        # Step 3: Check visibility of logout link
        assert inventory_page.is_element_visible(inventory_page.LOGOUT_LINK)

        # Step 4: Perform logout and verify redirection to login
        inventory_page.logout()
        assert login_page.is_element_visible(LoginPage.USERNAME_INPUT)
    finally:
        driver.quit()
