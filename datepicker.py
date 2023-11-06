from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)


# driver.get("https://jqueryui.com/datepicker")
# driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='content']/iframe"))

# date_field = driver.find_element(By.ID, "datepicker")
# date_field.click()

# # Clear the existing date value (if any)
# date_field.send_keys(Keys.CONTROL + "a")  # Select all text
# date_field.send_keys(Keys.DELETE)  # Delete the selected text

# # Set the desired date
# date_field.send_keys("02/01/2023")

# time.sleep(3)


driver.get("https://demoqa.com/date-picker")
# driver.find_element(By.ID, "datePickerMontYearInput").clear()
driver.find_element(By.ID, "datePickerMonthYearInput").click()
pyautogui.press('backspace', presses=10)
time.sleep(3)
driver.find_element(By.ID, "datePickerMonthYearInput").send_keys("02/01/2021")