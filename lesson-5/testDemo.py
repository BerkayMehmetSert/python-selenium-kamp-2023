from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from pathlib import Path
from datetime import date


class TestDemoClass:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        # get today's date and check if there is a folder with this date if not create it
        self.folder_path = str(date.today())  # 2023-03-24
        Path(self.folder_path).mkdir(exist_ok=True)  # folder is created if it does not exist

    def teardown_method(self):
        self.driver.quit()

    # setup_method -> test_demo_function -> teardown_method
    def test_demo_function(self):
        # 3A - Arrange, Act, Assert
        text = "Hello"
        assert text == "Hello"

    # setup_method -> test_demo_function2 -> teardown_method
    def test_demo_function2(self):
        assert True

    # setup_method -> test_valid_login -> teardown_method
    # @pytest.mark.skip(reason="Why this test is not working?")
    @pytest.mark.parametrize("username,password", [("1", "1"), ("2", "2")])
    def test_invalid_login(self, username, password):
        # max 5 seconds to find the element visible on the page before throwing an exception
        self.wait_for_element_visible((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")

        self.wait_for_element_visible((By.ID, "password"), 10)
        password_input = self.driver.find_element(By.ID, "password")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")

        # save screenshot
        self.driver.save_screenshot(f"{self.folder_path}/test_invalid_login_{username}_{password}.png")

        assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

    def wait_for_element_visible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
