from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print("Hello World")
driver = webdriver.Ie(
    "C:\\Users\\Mandar_rane\\Desktop\\care\\Installs\\IEDriverServer.exe")
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("http://www.yahoo.com/")
window_before = driver.window_handles[0]
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
print("script finished")

time.sleep(10)
below part is not yet working
print(len(driver.window_handles))
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
driver.get('http://stackoverflow.com/')
driver.navigate
