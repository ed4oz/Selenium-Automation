from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import Keys
from time import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window() 
driver.implicitly_wait(30)
driver.get("http://www.apple.com")
sleep(3)
print(driver.title)
# print(driver.current_window_handle)
apple=driver.current_window_handle
driver.switch_to.new_window("tab")
# driver.switch_to.new_window("window")
driver.get("http://www.tesla.com")
sleep(3)
print(driver.title)
# print(driver.current_window_handle)
# print(driver.window_handles)
tesla=driver.window_handles[1]
driver.switch_to.window(apple)
print(driver.title)
sleep(2)
driver.switch_to.window(tesla)
print(driver.title)
sleep(2)
driver.switch_to.window(apple)
sleep(1)
