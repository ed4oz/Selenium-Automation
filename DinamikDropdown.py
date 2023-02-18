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

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window() 
driver.implicitly_wait(15)
driver.get("http://www.ucuzabilet.com")

nereden=driver.find_element(By.ID, "from_text")
nereden.send_keys("avust")
sleep(2)
graz= driver.find_element(By.XPATH, "//li[contains(text(), 'GRZ')]")
graz.click()
sleep(2)

## select kullanmıyoruz. web element gibi kullanıyoruz statik olandan farklı