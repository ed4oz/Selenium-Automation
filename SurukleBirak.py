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
driver.implicitly_wait(30)
driver.get("https://demoqa.com/droppable/")


kaynak= driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div")
hedef= driver.find_element(By.CSS_SELECTOR,"div#simpleDropContainer div.drop-box" )

print("Once:"+ hedef.text)
action= ActionChains(driver)
action.drag_and_drop(kaynak, hedef).perform() #sürükle ve bırak
sleep(2)
print("Sonra:"+hedef.text)
sleep(2)