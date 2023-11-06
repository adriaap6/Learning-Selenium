from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://demoqa.com/select-menu")

# old style selection
driver.find_element(By.ID, "oldSelectMenu")

pilih = Select(driver.find_element(By.ID, "oldSelectMenu"))
pilih.select_by_visible_text('Aqua')

# select one with typing
driver.find_element(By.ID, "selectOne").click()
pyautogui.typewrite('Prof.')
pyautogui.press('enter')