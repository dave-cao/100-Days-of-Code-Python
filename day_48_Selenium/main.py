from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/cow/Documents/System/Development/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)


driver.get("https://www.python.org/")

events = driver.find_elements(
    by=By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li'
)

events_object = {
    i: {"time": event.text.split("\n")[0], "name": event.text.split("\n")[1]}
    for i, event in enumerate(events)
}

print(events_object)
driver.quit()
