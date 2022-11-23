from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR,"#cookie")

# Get current money  = cookie count
money = driver.find_element(By.CSS_SELECTOR,"#money").text
if "," in money:
    money = money.replace(",","")
money = int(money)

# Make lists with the upgrades (items and price) that could be bought
upgrades = driver.find_elements(By.CSS_SELECTOR,"#store b")
item_list = []
price_list =[]
for upgrade in upgrades:
    element_text = upgrade.text
    if element_text != "":
        item = element_text.split("-")[0].strip()
        item_list.append(item)
        price = int(upgrade.text.split(" - ")[1].strip().replace(",",""))
        price_list.append(price)
print(item_list)
print(price_list)



timeout = time.time() + 60 * 5
while True:
    cookie.click()
    if time.time() > timeout:
        break









time.sleep(5000)