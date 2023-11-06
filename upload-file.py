from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
# alamat 1
driver.get("https://demoqa.com/upload-download")

# alamat 2
# driver.get("https://gofile.io/uploadFiles")

# cara 1
driver.find_element(By.ID, "uploadFile").send_keys("D:/Adria Tisnawati A/QA Polindra/reverse perpus.pdf")

# cara 2
# driver.find_element(By.ID, "uploadFile").click()
# time.sleep(3)

# pyautogui.write("D:\Adria Tisnawati A\QA Polindra\reverse perpus.pdf")
# pyautogui.press("enter")

