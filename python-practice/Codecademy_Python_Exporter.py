from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import getpass
import time 


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://www.codecademy.com/login')
if "Log in | Codecademy" in driver.title:
    print("Login link opened successfully")

print("Finding User Name and Password Text boxes")
username = driver.find_element_by_id("user_login")
password = driver.find_element_by_id("user_password")

print("Accepting user name and password from user as raw_input")
username_input = input("Enter a user name: ")
password_input = getpass.getpass("Enter a user password: ") #getpass does not work on sublime https://github.com/wuub/SublimeREPL/issues/374
#password_input = input("Enter a user password: ")
username.send_keys(username_input)
password.send_keys(password_input)

print("Finding login btn and submiting user id and password")
loginbtn = driver.find_element_by_id("user_submit")
loginbtn.click()

if "Log in | Codecademy" in driver.title:
    print("Still at the login page, checking if any error")
    error_ele = driver.find_element_by_class_name("field-error")
    if "Invalid login or password." in error_ele.text:
        print("Login Failed with error 'Invalid login or password.'")
else:
    print("Verifying if login successfull or not")
    if "Learn | Codecademy" in driver.title:
        print("Browser Title is now 'Learn | Codecademy'")
        if 'https://www.codecademy.com/learn' == driver.current_url:
            print("Browser link is now 'https://www.codecademy.com/learn'")
            print("Finding image link that opens user profile window ")
            userdropdown = driver.find_element_by_id("dropdown-toggle")
            print("Clicking the image link that opens user profile window ")
            userdropdown.click()
            print("Finding user logout btn")
            logoutbtn = driver.find_element_by_id("sign-out-link")
            time.sleep(10)  
            logoutbtn_text = str(logoutbtn.text)
            logoutbtn_innerhtml = str(logoutbtn.get_attribute("innerHTML"))
            print("Found logout bttn, text in logoutbtn is:" + logoutbtn_text)
            print("Found logout bttn, innerhtml in logoutbtn is:" + logoutbtn_innerhtml)
            if 'Log out' in logoutbtn_innerhtml:
                print("Logout btn is now available, hence Login is successfull")
            else:
            	print("Something went wrong")


print("closing driver")
driver.close()
# html = driver.page_source

# soup = BeautifulSoup(html)

# for tag in soup.find_all('title'):
#     print(tag.text)


def get_all_python_chapter_urls(course_url):
    page = urlopen(course_url)
    soup = BeautifulSoup(page.read(), "html.parser")
    print(soup.name)
    all_links = soup.find_all("a", "link--target")
    f = open("PythonChapterLinks.txt", "w")
    print("all_link variable is of type")
    print(type(all_links))
    # print("printing all links")
    # print(all_links)
    for al in all_links:
        f.write("https://www.codecademy.com" + str(al['href']) + "\n")
    print(
        "All python chapter links are now stored in PythonChapterLinks.txt" + "\n")
    f.close
    print("Printing contents of PythonChapterLinks.txt" + "\n")
    f = open("PythonChapterLinks.txt", "r")
    print(f.read())
    print("Closing PythonChapterLinks.txt" + "\n")
    f.close


def get_all_chapter_topic_urls(chapter_url):
    print(chapter_url)
    page = urlopen(chapter_url)
    soup = BeautifulSoup(page.read(), "html.parser")
    print(soup.name)
    all_links = soup.find_all("a")
    f = open("PythonChapterTopicLinks.txt", "w")
    print("all_link variable is of type")
    print(type(all_links))
    # print("printing all links")
    # print(all_links)
    for al in all_links:
        print(al['href'])
        #f.write("https://www.codecademy.com" + str(al['href']) + "\n")
    print(
        "All python chapter topic links are now stored in PythonChapterTopicLinks.txt" + "\n")
    f.close
    print("Printing contents of PythonChapterTopicLinks.txt" + "\n")
    f = open("PythonChapterTopicLinks.txt", "r")
    print(f.read())
    print("Closing PythonChapterTopicLinks.txt" + "\n")
    f.close

# course_url = 'https://www.codecademy.com/learn/python'
# get_all_python_chapter_urls(course_url)

# visit one chapter at a time and get all chapter topic links
# chapter_url = 'https://www.codecademy.com/en/courses/introduction-to-python-6WeG3/resume?curriculum_id=4f89dab3d788890003000096'
# get_all_chapter_topic_urls(chapter_url)

# visit one chapter and one chapter topic at a time and get topic description and instruction
# If you only want the text part of a document or tag, you can use the
# get_text() method. It returns all the text in a document or beneath a
# tag, as a single Unicode string:


# visit one chapter and one chapter topic at a time and get topic code
