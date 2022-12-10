import time
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Scrape zillow for job listings

google_form_link = "https://forms.gle/WWEG5QFhHJWAmKKWA"
CHROME_DRIVE_PATH = "/home/cow/Documents/System/Development/chromedriver"

# 1. Use beautiful soup to get all the links from the listings you scraped
headers = {
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
}

print("Getting data from page...")
response = requests.get(
    "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=headers,
)

soup = BeautifulSoup(response.text, "html.parser")

# Get all the listings from the current webpage
rental_listings = soup.find_all(name="a", class_="property-card-link", href=True)
links = []
addresses = []
for i, listing in enumerate(rental_listings):
    # take into account the double links
    if not i % 2:
        # some links don't have the https:// back link
        if listing["href"][0] == "h":
            links.append(listing["href"])
        else:
            links.append(f"https://www.zillow.com{listing['href']}")

        addresses.append(listing.text)


rental_prices = soup.find_all(
    name="div", class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 hRqIYX"
)
prices = [price.text for price in rental_prices]


print("Opening Selenium...")
s = Service(CHROME_DRIVE_PATH)
driver = webdriver.Chrome(service=s)

for i in range(len(prices)):
    print("Opening google form...")
    driver.get(google_form_link)

    time.sleep(2)
    address_input = driver.find_element(
        by=By.XPATH,
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    price_input = driver.find_element(
        by=By.XPATH,
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    link_input = driver.find_element(
        by=By.XPATH,
        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )

    print("Filling in answers...")
    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])
    time.sleep(1)

    print("Submit form...")
    submit_button = driver.find_element(
        by=By.XPATH,
        value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span",
    )
    submit_button.click()
    time.sleep(1)

print("Program has ended...have a good day!")
