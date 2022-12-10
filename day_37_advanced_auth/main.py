import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "asdgasdghalskdhval"
USERNAME = "davidcao"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
today = datetime.date.today() - datetime.timedelta(days=1)
print(today)


graph_config = {
    "id": GRAPH_ID,
    "name": "Studying Graph",
    "unit": "Hrs",
    "type": "int",
    "color": "momiji",
}

headers = {"X-USER-TOKEN": TOKEN}

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20",
}

pixel_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_config['date']}"
)

response = requests.delete(url=pixel_endpoint, headers=headers)
print(response.text)
