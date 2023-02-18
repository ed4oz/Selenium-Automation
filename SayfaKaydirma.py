from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import *
from selenium.webdriver.support.select import Select

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window() 
driver.get("https://www.lovehomeswap.com/blog/destinations-inspiration/the-50-most-visited-tourist-attractions-in-the-world")
driver.execute_script("window.scrollBy(0,300)", "")
sleep(3)
driver.execute_script("window.scrollBy(0,3000)", "")
sleep(3)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
istanbul=driver.find_element(By.PARTIAL_LINK_TEXT, "Grand Bazaar,")
driver.execute_script("arguments[0].scrollIntoView()", istanbul)
driver.execute_script("window.scrollBy(0,-200)", "")
sleep(3)

