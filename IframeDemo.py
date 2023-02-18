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
# iframe=bir html sayfasının içinde başka bir html dosyası olması
#1.iframe id
#2.iframe name
#3.index(0dan başlıyor) bu üçünü kullanabilirz

#bir frame e switch ile geçiyor ve tekrar iframeden çıkarmamız lazım.
#default_content sayfanın aslına döner
#parent_frame bir üstteki frame e geçiş yapıyor

driver.get("https://tomspizzeria.herokuapp.com/iframe-demo.html")
# 1. iframe id
# 2. iframe name
# 3 index (0'dan basliyor')
driver.switch_to.frame(0)
driver.find_element(By.ID, "email").send_keys("brad.pitt@fil.com")
time.sleep(2)
# default_content => en ana sayfaya don,, sayfanin aslina don
# parent_frame => bir ustteki frame gecis icin
# 1. ana sayfa
#   2. frame 1
#      3 frame 2
driver.switch_to.default_content()
driver.find_element(By.ID, "isim").send_keys("angelina.jolie@film.com")
time.sleep(2)

driver.quit()