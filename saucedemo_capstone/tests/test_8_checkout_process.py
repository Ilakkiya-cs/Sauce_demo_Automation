"""
Tests the complete checkout flow and captures a screenshot.
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.driver_factory import DriverFactory


def test_checkout_process():
    """
    Full checkout flow including product match and screenshot capture.
    """
    driver = DriverFactory.get_driver()
    try:
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Step 2: Add 4 random products
        inventory_page = InventoryPage(driver)
        selected = inventory_page.select_random_products(count=4)
        selected_items = []
        for item in selected:
            name, price = inventory_page.fetch_product_info(item)
            selected_items.append((name, price))
            inventory_page.add_product_to_cart(item)

        # Step 3: Proceed to cart
        inventory_page.open_cart()
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

        # Step 4: Fill checkout form
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_checkout_info("John", "Doe", "12345")

        # Step 5: Screenshot of overview
        checkout_page.capture_checkout_overview_screenshot()

        # Step 6: Match overview product details
        overview_items = checkout_page.get_overview_items()
        for item in selected_items:
            assert item in overview_items

        # Step 7: Finish order and confirm
        confirmation = checkout_page.finish_order()
        assert "THANK YOU FOR YOUR ORDER" in confirmation.upper()

    finally:
        driver.quit()
