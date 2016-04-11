from selenium import webdriver


driver = webdriver.Chrome(executable_path=".\\chromedriver.exe", service_args=["--verbose", "--no-sandbox", "--log-path=.\\qc1.log"])




driver.get("http://gabautomation.usefedora.com/courses/webdriverpython/lectures/35508")
driver.quit()