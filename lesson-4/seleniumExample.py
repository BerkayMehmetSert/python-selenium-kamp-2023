from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# ChromeDriverManager().install() will download the latest version of ChromeDriver and save it to the cache.
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()  # Maximize the window

driver.get("https://www.google.com")  # Open Google

# HTML Locator
input = driver.find_element(By.NAME, "q")  # Find the search box

input.send_keys("kodlamaio")  # Enter the search term

sleep(2)  # Wait 2 seconds

search_button = driver.find_element(By.NAME, "btnK")  # Find the search button

search_button.click()  # Click the search button

sleep(2)  # Wait 2 seconds

# Find the first result
first_result = driver.find_element(By.XPATH,
                                   "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a")

sleep(2)  # Wait 2 seconds

first_result.click()  # Click the first result

list_of_courses = driver.find_elements(By.CLASS_NAME, "course-listing")  # Find all courses

print(f"kodlama.io has {len(list_of_courses)} courses")  # Print the number of courses

# infinite loop to keep the browser open
while True:
    continue
