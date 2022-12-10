# Looking for Amazon Pricing
import os
import smtplib
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASS = os.environ["MY_PASS"]

url = "https://www.amazon.ca/Professional-Irrigator-Adjustable-Countertop-Replaceable/dp/B09MQJ8PFB/?_encoding=UTF8&pd_rd_w=G9PY8&content-id=amzn1.sym.9999b127-1f9a-429f-9ac1-521e1f6b859e&pf_rd_p=9999b127-1f9a-429f-9ac1-521e1f6b859e&pf_rd_r=RXP5PJK0CJW9JKM8RGDG&pd_rd_wg=dbjX1&pd_rd_r=48e4098e-cbe4-4877-93b2-d3a01a28c3c0&ref_=pd_gw_ci_mcx_mi"
headers = {
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
}
response = requests.get(url, headers=headers)
amazon_page = response.text

soup = BeautifulSoup(response.text, "lxml")
tags = soup.find_all(name="span", class_="a-offscreen")


# grab text from tags
texts = [tag.get_text() for tag in tags]

# filter out text
current_price = float(texts[0][1:])
set_low = 45

# Send an email when the price is low enough (let's revisit this later)
if current_price < set_low:
    print("sent email")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Low Price Alert!\n\nThe price of the electric flosser is {current_price} and set low is {set_low}!",
        )
else:
    print("Not low today")
