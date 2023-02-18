from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import *

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.duckduckgo.com")
driver.maximize_window()
aramakutusu1 = driver.find_element(By.CSS_SELECTOR, "#search_form_input_homepage" )
aramakutusu1.send_keys("Selenium")
driver.find_element(By.ID, "search_button_homepage").click()
driver.find_element(By.ID, "r1-1").click()
#bazı yerlerde click yerine enter kullanmak gerekebilir çünkü bazen buton sonuçların arkasında kalabiliyor


