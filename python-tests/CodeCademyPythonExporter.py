from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get('https://www.codecademy.com/login')
username = selenium.find_element_by_id("user_login")
password = selenium.find_element_by_id("user_password")

username.send_keys(raw_input())
password.send_keys(raw_input())
selenium.find_element_by_name("user_submit").click()



html = driver.page_source

soup = BeautifulSoup(html)

for tag in soup.find_all('title'):
print tag.text






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
    print("All python chapter topic links are now stored in PythonChapterTopicLinks.txt" + "\n")
    f.close
    print("Printing contents of PythonChapterTopicLinks.txt"+"\n")
    f = open("PythonChapterTopicLinks.txt", "r")
    print(f.read())
    print("Closing PythonChapterTopicLinks.txt"+"\n")
    f.close

# course_url = 'https://www.codecademy.com/learn/python'
# get_all_python_chapter_urls(course_url)

# visit one chapter at a time and get all chapter topic links
chapter_url = 'https://www.codecademy.com/en/courses/introduction-to-python-6WeG3/resume?curriculum_id=4f89dab3d788890003000096'
get_all_chapter_topic_urls(chapter_url)

# visit one chapter and one chapter topic at a time and get topic description and instruction
# If you only want the text part of a document or tag, you can use the get_text() method. It returns all the text in a document or beneath a tag, as a single Unicode string:


# visit one chapter and one chapter topic at a time and get topic code
