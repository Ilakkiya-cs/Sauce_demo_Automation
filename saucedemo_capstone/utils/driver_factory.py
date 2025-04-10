from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException


class DriverFactory:
    """
    A factory class to initialize WebDriver instances.
    """

    @staticmethod
    def get_driver():
        try:
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")

            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.implicitly_wait(10)
            return driver

        except WebDriverException as e:
            raise Exception(f"WebDriver could not be initialized: {str(e)}")
