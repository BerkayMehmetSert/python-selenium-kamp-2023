from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestSauce:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        # max 5 seconds to find the element visible on the page before throwing an exception
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        username_input = self.driver.find_element(By.ID, "user-name")

        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        password_input = self.driver.find_element(By.ID, "password")

        username_input.send_keys("1")
        password_input.send_keys("1")

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert error_message.text == "Epic sadface: Username and password do not match any user in this service"


    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")  # refresh the page

        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        username_input = self.driver.find_element(By.ID, "user-name")

        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        password_input = self.driver.find_element(By.ID, "password")

        # Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(username_input, "standard_user")  # send keys to the username input
        actions.send_keys_to_element(password_input, "secret_sauce")  # send keys to the password input
        actions.perform()  # execute the actions

        # username_input.send_keys("standard_user")
        # password_input.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        self.driver.execute_script("window.scrollTo(0, 500)")  # scroll to the bottom of the page


test_class = TestSauce()
test_class.test_invalid_login()
test_class.test_valid_login()
