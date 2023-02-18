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
driver.get("http://tomspizzeria.herokuapp.com/yeni-sekme.html")
facebook = driver.find_element(By.ID, "facebook").click()
twitter = driver.find_element(By.ID, "twitter").click()
instagram = driver.find_element(By.ID, "instagram").click()
time.sleep(2)

def sekme_degistir(baslik):
    for sayfa in driver.window_handles:
        driver.switch_to.window(sayfa)
        if baslik.lower() in driver.title.lower():
            break


sekme_degistir("facebook")
print("facebook: "+driver.title)

sekme_degistir("twitter")
print("twitter: "+driver.title)

sekme_degistir("instagram")
print("instagram: "+driver.title)

sekme_degistir("selenium")
print("anasayfa: "+driver.title)

#indexle sayfa değiştirmek çokta kullanışlı bir yöntem değil o yüzden bu şekilde fonksiyon oluşturup yapmak daha doğru. özellikle 2den fazla sekme değişmesi gerekiyorsa
