# A bot that plays the cookieclicker game for 5 minutes
import random
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

time_out = time.time() + 300
chrome_driver_path = "Your chrome driver path"
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

while True:

    cookie = driver.find_element(by=By.ID, value="bigCookie")
    cookie.click()

    cookie_numbers = int(driver.find_element(by=By.ID, value="cookies").text.split()[0].replace(",", " "))
    d = range(10)
    b = random.choice(d)
    try:
        clicker_price = int(driver.find_element(by=By.ID, value=f"productPrice{b}").text.split()[0].replace(",", ""))
    except IndexError:
        pass
    else:
        print(clicker_price)
        if cookie_numbers > int(clicker_price):
            try:
                clicker = driver.find_element(by=By.ID, value=f"product{b}")
                clicker.click()
            except ElementClickInterceptedException:
                b = random.choice(d)
            else:
                clicker = driver.find_element(by=By.ID, value=f"product{b}")
                clicker.click()

    if time.time() > time_out:
        print(f'cookies/second: {driver.find_element(by=By.ID, value="cookies").text.split()[5].replace(",", " ")}')
        break

