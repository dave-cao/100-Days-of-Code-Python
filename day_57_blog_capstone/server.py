from datetime import datetime

import requests
from flask import Flask, render_template

CURRENT_YEAR = datetime.today().year
MY_NAME = "David Cao"


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html", CURRENT_YEAR=CURRENT_YEAR, MY_NAME=MY_NAME)


@app.route("/guess/<name>")
def guess(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("guess.html", age=age, gender=gender, name=name.capitalize())


@app.route("/blog/<num>")
def get_blog(num):

    blog_posts = requests.get("https://api.npoint.io/58978e898d3115a0a34e").json()
    return render_template("blog.html", blog_posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
