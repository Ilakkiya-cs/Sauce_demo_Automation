"""
Handles product selection and navigation from the inventory page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random


class InventoryPage(BasePage):
    """
    Page class for the Inventory Page.
    """
# locators
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.XPATH, ".//button[contains(text(), 'Add to cart')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_all_inventory_items(self):
        """
        Fetches all inventory item elements.
        """
        return self.find_elements(self.INVENTORY_ITEMS)

    def select_random_products(self, count=4):
        """
        Randomly selects number of products and returns their elements.
        """
        all_items = self.get_all_inventory_items()
        return random.sample(all_items, count)

    def fetch_product_info(self, product_element):
        """
        Fetches product name and price from a given product element.
        """
        name = product_element.find_element(*self.ITEM_NAME).text
        price = product_element.find_element(*self.ITEM_PRICE).text
        return name, price

    def add_product_to_cart(self, product_element):
        """
        Clicks 'Add to cart' button for the given product element.
        """
        product_element.find_element(*self.ADD_TO_CART_BUTTON).click()

    def get_cart_count(self):
        """
        Returns the number of items shown in the cart.
        """
        if self.is_element_visible(self.CART_BADGE):
            return int(self.get_element_text(self.CART_BADGE))
        return 0

    def open_cart(self):
        """
        Clicks on the cart icon to navigate to cart.
        """
        self.click_element(self.CART_ICON)

    def open_logout_menu(self):
        """
        Opens the burger menu.
        """
        try:
            # Standard click fails if intercepted
            self.click_element(self.BURGER_MENU)
        except Exception:
            # Fallback: click using JavaScript
            menu_button = self.driver.find_element(*self.BURGER_MENU)
            self.driver.execute_script("arguments[0].click();", menu_button)

    def logout(self):
        """
        Logs out of the application.
        """
        self.open_logout_menu()
        self.click_element(self.LOGOUT_LINK)
