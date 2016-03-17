from selenium import webdriver
print("Hello World")
# driver = webdriver.Ie(
# "C:\\Users\\abcd\\Desktop\\efgh\\Installs\\IEDriverServer.exe")
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.yahoo.com/")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
print("script finished")

