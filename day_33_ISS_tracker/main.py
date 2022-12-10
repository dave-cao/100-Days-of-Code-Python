import smtplib
from datetime import datetime

import requests

from config import my_data

MY_LAT = 53.544388
MY_LNG = -113.490929

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


within_area = (
    MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
    and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5
)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if within_area and ((hour_now >= sunset) or (hour_now <= sunrise)):
    # send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_data["email"], password=my_data["password"])
        connection.sendmail(
            from_addr=my_data["email"],
            to_addrs=my_data["email"],
            msg="Subject:ISS Overhead!\n\nLook up! The International Space Station is over your head right now!",
        )
