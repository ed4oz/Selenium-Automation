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
#time.sleep kullanmanın dezavantajları olabilir. çünkü sleep süresi yüklenme süresinden az olabilir ve hata verebilir.
#ya da tam tersi durumda boşu boşuna beklemesi gerekir. testin bitmesi de uzun sürecek
#2 çeşit bekleme yöntemi veriyor selenium
#1-implicit wait - gizli bekleme
#driver nesnesi ile çalışır. en son kullanılan geçerli olacak eğer birden fazla kullanılırsa
# # driver.implicitly_wait(20) #bulamazsa 20 sn bekleyecek ve 20 sn içinde bulmaya çalışacak
driver.get("https://pynishant.github.io/Selenium-python-waits.html")
#2-explicit wait- açıktan bekleme
tryit=driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver, 45).until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))
clickme=driver.find_element(By.XPATH, "//button[contains(text(), 'CLICK ME')]").click()

#presence vs visibility kullancıya görünür olmayabilir web element o durumda presence tercih edilir. görünür olup olmadığına bakmak içinde visibility kullanılıyor 
#url_changes mesela yükleme tamamlandığında url değişecek burdan anlaşılabilir. buna bakabiliriz 

#3-fluent wait seleniumun kendisi yarım saniyede bir bakıyor. ne kadar bekleyeceğini bizde ayarlayabilirz
# WebDriverWait(driver, 45,0.1,ignored_exceptions=[NoSuchElementException, NotClickableException]).until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))


# 1. Implicitly wait (Gizli bekleme): 
# Bu bekleme türü WebDriver nesnesinin bir özelliğidir ve o Webdriver nesnesi var olduğu sürece geçerli olacaktır. WebDriver nesnesini oluşturduğumuzda driver.implicitly_wait(30) şeklinde belirteceğimiz bekleme tüm proje boyunca aktif olacaktır. Şayet daha sonra yine driver.implicitly_wait(10) şeklinde deklare edersek Selenium öncekini yok sayacak ve artık 10 saniye bekleyecektir. Biz bir kere deklare ettikten sonra arka planda bizim için element bulurken hata vermeden önce belirttiğimiz süre kadar elementi bulmaya çalışacaktır. Bu süre zarfında bulamazsa o zaman hata verecektir. 

# 2. Explicit wait (Açıktan bekleme)
# Adından da anlaşılacağı gibi implicit wait için belirttiğimiz süre yetersiz kalabilir diye düşünürsek o durumda farklı bir beklemeye ihtiyacımız olacak. Bu durumda belli bir şart sağlanana kadar beklememiz gerekecek. Explicit wait element düzeyinde kullanılır ve her seferinde yeniden deklare etmek gerekir. 

#Alert() classı oluşturulmuş
WebDriverWait(driver,3).until(expected_conditions.alert_is_present())
uyarı=Alert(driver)
sleep(3)
uyarı.accept()