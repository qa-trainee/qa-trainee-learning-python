from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.implicitly_wait(5)
# You are telling the DOM to search for an element within a period which is defined as 5 above
# The period remains same till u quit the driver.
# No Such element exception if can not find the ilement.

driver.get("https://www.google.com")

searchField = driver.find_element_by_css_selector("input[name=q]")
searchField.send_keys("ABCSD")
sleep(5)



driver.quit()