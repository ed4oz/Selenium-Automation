from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import *

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.duckduckgo.com")
sleep(5)
# driver.maximize_window()
# aramakutusu= driver.find_element(By.ID,"search_form_input_homepage")
# aramakutusu.send_keys("python")
# aramakutusu.send_keys(Keys.ENTER)
# sleep(3)

driver.get("http://www.google.com")
aramakutusu=driver.find_element(By.NAME, "q")
aramakutusu.send_keys("Selenium")
aramakutusu.send_keys(Keys.ENTER)

