from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # untuk membuka tab agar tidak force closed

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.ID, "username").send_keys("adria") #cara 1
element.send_keys("adria")

element = driver.find_element(By.NAME, "username") #cara 3
element.send_keys("sibad")

element = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
element.click()

h2 = driver.find_element(By.TAG_NAME, "h2")
print(h2)

element = driver.find_element(By.CLASS_NAME, "radius").click() #cara2
element.click()

element = driver.find_element(By.CSS_SELECTOR, "button.radius")
element.click()

element = driver.find_element(By.XPATH, "//*[@id='content']/div/button")
element.click()

