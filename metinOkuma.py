from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import *

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
seckin_madde_alanı=driver.find_element(By.ID, "mp-tfa")
seckin_madde_yazisi=seckin_madde_alanı.text
seckin_madde_yazisi = seckin_madde_yazisi.split(",")[0]
print("seçkin madde: "+ seckin_madde_yazisi)
kaliteli_madde=driver.find_element(By.ID, "mf-tfp").text
kaliteli_madde = kaliteli_madde.split(",")[0]
print("kaliteli madde: "+ kaliteli_madde)