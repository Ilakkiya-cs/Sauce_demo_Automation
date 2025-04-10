"""
Tests login failure using invalid credentials.
"""

import pytest
from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory

def test_invalid_login_guvi_user():
    """
       Attempt login with invalid credentials and verify error message appears.
       """
    driver = DriverFactory.get_driver()
    try:
        login_page = LoginPage(driver)
        login_page.login("guvi_user", "Secret@123")
        # Assert that login failed with an error message
        assert login_page.is_login_error_displayed()
    finally:
        driver.quit()
