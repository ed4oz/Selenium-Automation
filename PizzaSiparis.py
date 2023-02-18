from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import *
from selenium.webdriver.support.select import Select

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window() 
driver.get("https://tomspizzeria.b4a.app/")
def siparisver():
    driver.find_element(By.ID, "siparis").click()

def mesajoku():
    return driver.find_element(By.ID, "mesaj").text
#müsteri ismi
siparisver()
mesaj=mesajoku()
assert mesaj == "Müşteri ismi girmediniz"
#müşteri ismi girmediniz
#pizza boyu
#pizza boyu seçmediniz
isim = "Tom Cruise"
driver.find_element(By.ID, "musteri-adi").send_keys(isim)
siparisver()
mesaj = mesajoku()
assert mesaj == "Pizza boyu seçmediniz"

#odeme sekli 
#odeme sekli seçmediniz
driver.find_element(By.CSS_SELECTOR, "input[value='Küçük']").click()
siparisver()
mesaj = mesajoku()
assert mesaj == "Ödeme tipi seçmediniz"


#sipariş alındı
dropdown=driver.find_element(By.ID, "odeme-tipi")
odeme=Select(dropdown)
odeme.select_by_index(2)
siparisver()
mesaj=mesajoku()
assert mesaj == "Siparişiniz alındı"

musteri=driver.find_element(By.ID, "musteri").text
boy  = driver.find_element(By.ID,"pizzaboyu").text
ek = driver.find_element(By.ID, "pizzaustu").text
odeme = driver.find_element(By.ID, "odeme").text
tutar=driver.find_element(By.ID, "tutar").text

assert musteri == "Müşteri ismi: "+ isim
assert boy == "Pizza boyu: Küçük"
assert ek == "Pizza üstü:"
assert odeme ==   "Ödeme tipi: Kredi Kartı"
assert tutar == "Tutar: 10 TL"

driver.execute_script("window.scrollBy(0,150)", "") #aşağı kaydırır
sleep(1)
driver.execute_script("window.scrollBy(0,-150)", "") #yukarı kaydırır 
sleep(2)

driver.save_screenshot("./sonuc.png")
