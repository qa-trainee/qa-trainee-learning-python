from selenium import webdriver
from time import sleep

##Chrome
## troubleshooting options include, update driver, chrome, check paths, verbose, no sandbox, no extensions etc
# from selenium.webdriver.chrome.options import Options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--disable-extensions')
# driver = webdriver.Chrome(executable_path=".\\chromedriver.exe",chrome_options=chrome_options, service_args=["--verbose", "--no-sandbox", "--log-path=.\\qc1.log"]) #does not work most probably due to admin rights

#  ##Firefox
# driver = webdriver.Firefox()

#  ##IE
driver = webdriver.Ie()

driver.get("https://www.google.com")
sleep(5)
driver.quit()