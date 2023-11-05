from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # untuk membuka tab agar tidak force closed

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/alerts")

driver.find_element(By.ID, "alertButton").click()
time.sleep(2)
# driver.switch_to.alert.accept()

try:
    alert = driver.switch_to.alert
    alert.accept()
except NoAlertPresentException:
    print("No alert was present.")