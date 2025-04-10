"""
Verifies items in the cart after adding them.
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.driver_factory import DriverFactory


def test_cart_product_details():
    """
    Adds 4 random products and verifies cart contains those items.
    """
    driver = DriverFactory.get_driver()
    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        selected = inventory_page.select_random_products(count=4)

        selected_names = []
        for product in selected:
            name, _ = inventory_page.fetch_product_info(product)
            inventory_page.add_product_to_cart(product)
            selected_names.append(name)

        inventory_page.open_cart()

        cart_page = CartPage(driver)
        cart_items = cart_page.get_cart_item_details()
        for name, price in cart_items:
            # Print all cart product details
            print(f"Cart Product: {name}, Price: {price}")

        cart_names = [name for name, _ in cart_items]

        for name in selected_names:
            assert name in cart_names
    finally:
        driver.quit()
