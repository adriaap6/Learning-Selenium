from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # untuk membuka tab agar tidak force closed

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/")

# driver.maximize_window()
driver.minimize_window()