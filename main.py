from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = driver.find_element(By.ID,"cookie")

#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [item.get_attribute("id") for item in items]

five_sec = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    #Every 5 seconds
    if time.time() > five_sec:
        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR,"#store div b")
        # Convert <b> text into an integer price.
        item_prices = [int(price.text.split("-")[1].strip().replace(",", "")) for price in all_prices if price.text != ""]
        # Create dictionary of store items and prices
        cookie_upgrades = {item_prices[n]: item_ids[n] for n in range(len(item_prices))}
        # Get current cookie count
        money_element = driver.find_element(By.ID,"money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
        # Find upgrades that we can currently afford
        affordable_upgrades ={cost: id for cost, id in cookie_upgrades.items() if cookie_count > cost}
        print(affordable_upgrades)
        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        buy_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(By.ID, buy_id).click()
        five_sec = time.time() + 5
    if time.time() > five_min:
        cookies_per_second = driver.find_element(By.ID, "cps")
        print(cookies_per_second.text)
        break
