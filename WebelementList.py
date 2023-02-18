from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import *

service= Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.imdb.com/")
driver.maximize_window()
driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()
sleep(1)
driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()
film_isimleri = driver.find_elements(By.XPATH, "//table//tbody/tr//td[@class='titleColumn']")

for i in film_isimleri:
    if i.text[-5:-1] == "2000":
        print(i.text)
    

# for i in range(20):
#     print(film_isimleri[i].text)

