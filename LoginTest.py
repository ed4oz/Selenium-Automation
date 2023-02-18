from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import *

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window

# #test otomasyon
# #beklentileri sağlıyor mu?
# #1.istenileni yapıyor mu? pozitif test
# #2.istenmeyeni yapıyor mu? negatif test
# #testçiler için bu ikisi de önemli o yüzden ikisini de kontrol edeceğiz

# #internet login sayfasına git https://the-internet.herokuapp.com/login
# driver.get("https://the-internet.herokuapp.com/login")
# #kullanıcı adını gir
# driver.find_element(By.ID, "username").send_keys("test")
# #şifre gir
# driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
# #log in düğmesine bas
# driver.find_element(By.CSS_SELECTOR,"button.radius").click()
# #yanlis kullanici adi Your username is invalid
# mesaj = driver.find_element(By.ID, "flash").text

# if "Your username is invalid!"in mesaj:
#     print("OK, yanlış kullanıcı adı doğru çalışıyor")
# else:
#     print("HATA: yanlış kullanıcı adı çalışmıyor.")

# #yanlış şifre girince: your password is invalid
# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element(By.ID, "username").send_keys("tomsmith")
# driver.find_element(By.ID,"password").send_keys("asdf")
# driver.find_element(By.CSS_SELECTOR,"button.radius").click()
# mesaj2=driver.find_element(By.ID,"flash").text
# print("Yanlış şifre mesajı:"+ mesaj2)
# if "Your password is invalid!"in mesaj2:
#     print("OK, yanlış şifre doğru çalışıyor")
# else:
#     print("HATA: yanlış şifre çalışmıyor.")
# #ikisidde doğru: mesaj; you logged into a secure area! link secure içerecek sayfada secure area
# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element(By.ID, "username").send_keys("tomsmith")
# driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
# driver.find_element(By.CSS_SELECTOR,"button.radius").click()
# mesaj3=driver.find_element(By.ID,"flash").text
# print("mesaj3:"+ mesaj3)
# if "You logged into a secure area!"in mesaj3:
#     print("OK")
# else:
#     print("HATA")

# link=driver.current_url
# if"secure" in link:
#     print("OK, link secure içeriyor")
# else:
#     print("HATA:link secure içermiyor")

# dogru_mesaj=driver.find_element(By.CSS_SELECTOR, "h2").text
# print("dogru mesaj:"+ dogru_mesaj)

# if "Secure Area" in dogru_mesaj:
#     print("OK")
# else:
#     print("HATA")
# #logout düğmesine tıklamak
# driver.find_element(By.XPATH, "//i[contains(text(), 'Logout')]").click()
# if "login" in driver.current_url:
#     print("OK")
# else:
#     print("HATA")

def login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,"button.radius").click()
    mesaj=driver.find_element(By.ID,"flash").text
    return mesaj

mesaj=login("asdf", "xyz")
assert "Your username is invalid!" in mesaj

# if "Your username is invalid!"in mesaj:
#     print("OK, yanlış kullanıcı adı doğru çalışıyor")
# else:
#     print("HATA: yanlış kullanıcı adı çalışmıyor.")

mesaj=login("tomsmith","xyz")
assert "Your password is invalid!" in mesaj
# if "Your password is invalid!"in mesaj:
#     print("OK, yanlış şifre doğru çalışıyor")
# else:
#     print("HATA: yanlış şifre çalışmıyor.")

mesaj=login("tomsmith","SuperSecretPassword!")
assert "You logged into a secure area!"in mesaj
# if "You logged into a secure area!"in mesaj:
#     print("OK")
# else:
#     print("HATA")

#birden fazla işlem yapılıyorsa fonksiyon yazıp yapmak işi kolaylaştırıyor.

