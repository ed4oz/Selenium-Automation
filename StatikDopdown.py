from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import *
from selenium.webdriver.support.select import Select

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window() 
#tıkladığımızda açılan listeler/açılır liste
driver.get("https://tomspizzeria.b4a.app/")
dropdown=driver.find_element(By.ID, "odeme-tipi")
odeme = Select(dropdown)
odeme_tipleri = odeme.options #web element listesi, her bir option tagi
for tip in odeme_tipleri:
    print(tip.text)
sleep(2)
odeme.select_by_visible_text("Kredi Kartı")
sleep(2)
odeme.select_by_index(3)
sleep(2)
