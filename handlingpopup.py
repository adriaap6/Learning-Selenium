from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)
driver.get("https://tees.co.id/")

for i in range(2):
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]")))
        print("pop up muncul")
        driver.find_element(By.CLASS_NAME, "btn-modal-close").click()
        print("pop up di close")
        
    except TimeoutException:
        print("pop up tidak muncul")
        pass
    time.sleep(3)