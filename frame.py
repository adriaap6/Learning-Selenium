from selenium import webdriver
from selenium.webdriver.common.by import By
from lib2to3.pgen2 import driver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame('frame-top')
driver.switch_to.frame('frame-left')

Text1 = driver.find_element(By.XPATH, '/html/body').text
print(Text1)

driver.switch_to.parent_frame()
driver.switch_to.frame('frame-middle')

Text2 = driver.find_element(By.XPATH, '//*[@id="content"]').text
print(Text2)