from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("http://demoqa.com")
print(driver.title)