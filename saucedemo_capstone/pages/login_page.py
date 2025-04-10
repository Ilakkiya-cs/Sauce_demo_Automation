"""
Handles login functionality for saucedemo.com
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page class for the Login Page of saucedemo.com
    """

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """
                Performs login by entering username and password and clicking the login button.
         """
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def is_login_error_displayed(self):
        """
        Checks if an error message is displayed after login attempt.
        """
        return self.is_element_visible(self.ERROR_MESSAGE)
