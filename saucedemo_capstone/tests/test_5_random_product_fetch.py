"""
Tests random selection of products and fetches their names and prices.
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.driver_factory import DriverFactory


def test_random_product_fetch():
    """
    Randomly select 4 products and fetch their names and prices.
    """
    driver = DriverFactory.get_driver()
    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        selected_products = inventory_page.select_random_products(count=4)

        assert len(selected_products) == 4

        for product in selected_products:
            name, price = inventory_page.fetch_product_info(product)
            # Print selected products' name and price
            print(f"Selected Product: {name}, Price: {price}")
    finally:
        driver.quit()
