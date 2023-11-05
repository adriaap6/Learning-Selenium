from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # untuk membuka tab agar tidak force closed

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/windows")

# PINDAH BROWSER TAB OTOMATIS
driver.find_element(By.LINK_TEXT, "Click Here").click()
driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.LINK_TEXT, "Click Here").click()
driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.LINK_TEXT, "Click Here").click()
driver.switch_to.window(driver.window_handles[0])

driver.find_element(By.LINK_TEXT, "Click Here").click()
driver.switch_to.window(driver.window_handles[0])