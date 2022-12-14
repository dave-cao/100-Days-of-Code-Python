import requests


class Post:
    def get_posts(self):
        return requests.get("https://api.npoint.io/58978e898d3115a0a34e").json()
