from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/alerts")

time.sleep(2)
driver.find_element(By.ID, "promtButton").click()
time.sleep(2)
driver.switch_to.alert.send_keys("saya sedang makan")
time.sleep(2)
driver.switch_to.alert.accept()
