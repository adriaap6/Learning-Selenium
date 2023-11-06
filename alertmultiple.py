from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/alerts")

# Scroll to the "confirmButton" element to make it clickable
confirm_button = driver.find_element(By.ID, "confirmButton")
driver.execute_script("arguments[0].scrollIntoView();", confirm_button)

# Click the button after scrolling
confirm_button.click()

# Handle the alert
alert = driver.switch_to.alert
alert.dismiss() # Cancel
