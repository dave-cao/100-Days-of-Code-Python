import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/cow/Documents/System/Development/chromedriver"
s = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/cow/.config/google-chrome/")
options.add_argument("profile-directory=Profile 6")

driver = webdriver.Chrome(service=s, options=options)

driver.get("https://tinder.com")


# Waiting until the browser loads
time.sleep(10)
while True:
    time.sleep(1)
    try:
        like = driver.find_element(
            by=By.TAG_NAME,
            value="body",
        )
        print("clicked")
        like.send_keys(Keys.ARROW_RIGHT)

    except NoSuchElementException:
        print("error happened")
        time.sleep(2)
        continue

time.sleep(20)
