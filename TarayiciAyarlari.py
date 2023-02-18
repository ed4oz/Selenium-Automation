from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import Keys
from time import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

service= Service("./chromedriver.exe")
options=Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-infobars")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-notifications") 
options.add_argument("--disable-save-password")
options.add_argument("--disable-extensions")
options.add_argument("download.default_directory=C:/kullanicilar/ali/test")
options.add_argument("--window-size=768,1024")
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window() 
driver.implicitly_wait(10)
driver.get("http://www.google.com")
sleep(2)
