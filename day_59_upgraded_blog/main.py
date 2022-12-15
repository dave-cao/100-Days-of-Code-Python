import os
import smtplib

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

# Upgraded Blog
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

blog_posts = requests.get("https://api.npoint.io/00fdf65805147ec97345").json()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route("/post/<post_id>")
def post(post_id):
    return render_template("post.html", post_id=int(post_id), blog_posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":

        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", sent_message=True)
    return render_template("contact.html", sent_message=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone Number: {phone}\nMessage: {message}"
    # send an email to myself if form is sent
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=email_message,
        )


if __name__ == "__main__":
    app.run(debug=True)
