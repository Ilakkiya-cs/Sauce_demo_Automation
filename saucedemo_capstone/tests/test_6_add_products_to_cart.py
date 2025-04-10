"""
Adds 4 random products to cart and verifies cart count.
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.driver_factory import DriverFactory


def test_add_products_to_cart():
    """
    Select and add 4 random products to cart, then verify cart item count.
    """
    driver = DriverFactory.get_driver()
    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        selected = inventory_page.select_random_products(count=4)

        for product in selected:
            inventory_page.add_product_to_cart(product)

        # Verify the cart badge shows '4'
        assert inventory_page.get_cart_count() == 4
    finally:
        driver.quit()
