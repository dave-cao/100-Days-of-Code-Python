import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/cow/Documents/System/Development/chromedriver"

s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")


# check right panel

seen = {}
seconds = 0
clicked = False
seen_clicked = {}
while True:
    now = int(time.time())
    cookie.click()
    minute = seconds / 60

    # start counting by seconds
    if now not in seen:
        seconds += 1
        seen[now] = None

    # make sure that right pane is only clicked once per 5 seconds
    if seconds not in seen_clicked:
        clicked = False

    # every 5 seconds check the right panel
    # click from button to top so that you can get most expensive first
    if not seconds % 5 and not clicked:
        store = driver.find_elements(
            by=By.CSS_SELECTOR, value="#store div:not(.grayed)"
        )
        store = store[::-1]
        try:
            for item in store:
                item.click()

        except:
            store = driver.find_elements(
                by=By.CSS_SELECTOR, value="#store div:not(.grayed)"
            )
            store = store[::-1]

        clicked = True
        seen_clicked[seconds] = None

    if minute == 5:
        per_second = driver.find_element(by=By.ID, value="cps")
        print(per_second.text)
