from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.apple.com")
link= driver.current_url
baslik= driver.title
print("sayfa basligi: "+ baslik)
if "apple.com" in link:
    print("Doğru apple sayfasındayız: " +link)
driver.maximize_window()
driver.get("http://www.etsy.com")
link= driver.current_url
baslik=driver.title
print("sayfa basligi: "+ baslik)
if "etsy.com" in link:
    print("Doğru etsy sayfasındayız: " + link)
driver.back()
baslik= driver.title 
driver.save_screenshot("./ekrangoruntusu.png")
if "Apple" in baslik:
    print("Tebrikler, Apple sayfasina dondun")
# else:
#     driver.save_screenshot("./ekrangoruntusu.png") 
#     test başarısız olduğunda o anda ekranda ne olduğunu görmek için kullanılır.
#suanki pencereyi kapatır. hangi sekmeyi yönetiyorsak onu kapatır
#driver.close()
#driver.quit ise seleniumun kullandığı tüm pencereleri kapatır. quiti kullanacağız iilerleyen zamanlarda
#driver.quit()



