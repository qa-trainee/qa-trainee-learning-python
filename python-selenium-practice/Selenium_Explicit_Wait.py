from selenium import webdriver
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
waiting = WebDriverWait(driver, 10) #Setting property for explicit wait timeout
driver.get("https://www.google.co.in")

print(datetime.now(), "Opened the website")

try:
	#searchField = driver.find_element_by_css_selector("input[name=q]")
	searchField = waiting.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name=qa]")))
	#Not sure why By requires additional ()
	print(datetime.now(), "Found search field, sending some text")
	searchField.send_keys("ABCSD")
	sleep(5)
finally:
	print(datetime.now(), "Exiting")
	driver.quit()


