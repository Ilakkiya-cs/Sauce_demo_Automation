"""
Handles the checkout process on saucedemo.com including form submission, order summary, and confirmation.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # ✅ <-- THIS LINE
from pages.base_page import BasePage
import os
import time



class CheckoutPage(BasePage):
    """
    Page class for the Checkout Page of saucedemo.com
    """
# locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    OVERVIEW_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def enter_checkout_info(self, first_name, last_name, zip_code):
        """
        Enters user info into the checkout form.
        """
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.ZIP_CODE, zip_code)
        self.click_element(self.CONTINUE_BUTTON)

    def capture_checkout_overview_screenshot(self, file_name="screenshots/checkout_overview.png"):
        """
        Captures a screenshot of the checkout overview page.
        """
        os.makedirs("screenshots", exist_ok=True)
        time.sleep(1)
        self.driver.save_screenshot(file_name)

    def get_overview_items(self):
        """
        Returns list of (name, price) for each item in overview.
        """
        self.wait.until(EC.visibility_of_all_elements_located(self.OVERVIEW_ITEMS))  # Add this
        items = []
        for item in self.find_elements(self.OVERVIEW_ITEMS):
            name = item.find_element(*self.ITEM_NAME).text
            price = item.find_element(*self.ITEM_PRICE).text
            items.append((name, price))
        return items

    def finish_order(self):
        """
        Clicks the finish button and returns confirmation text.
        """
        self.click_element(self.FINISH_BUTTON)
        return self.get_element_text(self.CONFIRMATION)
