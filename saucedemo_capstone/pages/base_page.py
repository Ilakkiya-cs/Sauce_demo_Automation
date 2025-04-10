"""
Base class for all Page Object classes.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException
)
from selenium.webdriver.common.by import By


class BasePage:
    """
    Base Page encapsulates all common methods for interacting with web elements
    using explicit waits and exception handling.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element(self, locator):
        """
              Clicks on a web element after waiting for it to be clickable.
             including a short delay to slow down the test visually.
              """
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except (TimeoutException, ElementNotInteractableException) as e:
            raise Exception(f"Unable to click on element {locator}: {str(e)}")

    def enter_text(self, locator, text):
        """
               Waits for a web element, clears any existing text, and enters the given text.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except (TimeoutException, ElementNotInteractableException) as e:
            raise Exception(f"Unable to enter text in element {locator}: {str(e)}")

    def get_element_text(self, locator):
        #  Waits for a web element and returns its visible text.
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            raise Exception(f"Unable to get text from element {locator}: {str(e)}")

    def is_element_visible(self, locator):
        # Returns True if the element becomes visible within the wait period.
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def find_elements(self, locator):
        #  Returns a list of elements matching the locator, or an empty list if none are found.
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []
