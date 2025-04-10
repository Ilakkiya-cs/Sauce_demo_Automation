"""
Handles cart operations like verifying added products and viewing their details.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page class for the Cart Page of saucedemo.com
    """
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items(self):
        """
        Returns all product elements present in the cart.
        """
        return self.find_elements(self.CART_ITEMS)

    def get_cart_item_details(self):
        """
        Returns list of (name, price) tuples for each item in the cart.
        """
        item_details = []
        for item in self.get_cart_items():
            name = item.find_element(*self.ITEM_NAME).text
            price = item.find_element(*self.ITEM_PRICE).text
            item_details.append((name, price))
        return item_details

    def proceed_to_checkout(self):
        """
        Clicks on the checkout button.
        """
        self.click_element(self.CHECKOUT_BUTTON)
