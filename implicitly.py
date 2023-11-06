from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://demoqa.com/login")
driver.get("https://demoqa.com/books")
driver.find_element(By.ID, "login").click()