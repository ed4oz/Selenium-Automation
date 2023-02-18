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
driver.get("https://the-internet.herokuapp.com/upload")
file = "C:/Users/Eda Özyurt/Desktop/SeleniumDemo/chromedriver.exe"
upload_file=driver.find_element(By.ID, "file-upload" )
sleep(5)
upload_file.send_keys(file)
upload_button=driver.find_element(By.ID, "file-submit").click()
WebDriverWait(driver, 30).until(expected_conditions.presence_of_all_elements_located((By.TAG_NAME, "h3")))
baslik= driver.find_element(By.TAG_NAME, "h3").text
print(baslik)
dosya=driver.find_element(By.ID, "uploaded-files").text
print(dosya)
sleep(2)
#File uploaded! h3
#id uploaded files