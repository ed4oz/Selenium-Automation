from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import Keys
from time import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

# service= Service("./chromedriver.exe") 
# driver = webdriver.Chrome(service=service)
# driver.maximize_window() 
# driver.get("http://www.fifa.com/")
# sleep(2) 