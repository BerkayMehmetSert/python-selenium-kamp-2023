from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class TestSauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        # max 5 seconds to find the element visible on the page (driver.implicitly_wait(5))
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        sleep(2)
        username_input.send_keys("1")
        password_input.send_keys("1")
        sleep(2)
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Error Message"
        print(f"The test result is: {test_result}")


test_class = TestSauce()
test_class.test_invalid_login()
