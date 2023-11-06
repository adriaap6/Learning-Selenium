from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging']) 

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/")