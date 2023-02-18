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
driver.get("https://the-internet.herokuapp.com/hovers")

user=driver.find_element(By.CSS_SELECTOR, "div.figure")
isim=driver.find_element(By.CSS_SELECTOR,"div.figcaption h5")
link=driver.find_element(By.CSS_SELECTOR, "div.figcaption a")

sleep(2)
hareket=ActionChains(driver)
hareket.move_to_element(user)
hareket.perform()

sleep(2)
print("----------")
print(user.is_displayed())
print("isim: "+isim.text)
link.click()
sleep(2)
url= driver.current_url
assert "users/1" in url
#fiziki olarak fare imlecini oynatmıyor. arka planda oynatarakgösteriyor