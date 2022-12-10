import requests

MY_LAT = 53.544388
MY_LNG = -113.490929
parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise, sunset)
