# import specialMath as math
from human import Human
from specialMath import summation as sum
import random  # built-in module
from selenium import webdriver  # external module

print(sum(10, 20))

print(random.randint(0, 100))

human1 = Human("Joe")
human1.talk("hello")

chrome_driver = webdriver.Chrome()
