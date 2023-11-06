from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/menu/")
driver.implicitly_wait(10)

# cara1
# menu = driver.find_element(By.LINK_TEXT, "Main Item 2")
# Hover = ActionChains(driver).move_to_element(menu)
# Hover.perform()

# Cara2
ActionChains(driver).move_to_element((driver.find_element(By.LINK_TEXT, "Main Item 2"))).perform()