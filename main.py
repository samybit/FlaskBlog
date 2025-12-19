# Standard library imports
import logging
import os
import smtplib
from datetime import datetime

# Third-party imports
import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for

logging.basicConfig(level=logging.INFO)

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# get all posts
all_posts = requests.get("https://api.npoint.io/abfbbb2fb46d6ccd9494").json()

app = Flask(__name__)

# get and inject current year
@app.context_processor
def inject_now():
    return {'year': datetime.now().year}


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


def send_email(name, email, phone, message):
    email_message = f"Subject: Flask Blog message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

    logging.info(f"Attempting to send email to {MY_EMAIL}...")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_message)

    logging.info("SMTP connection closed.")

# contact GET
@app.get('/contact')
def contact_form():
    # check if message has been sent -> if the URL has "?success=True"
    msg_sent = request.args.get('success')
    # Pass status to the HTML
    return render_template("contact.html", msg_sent=msg_sent)

# contact POST and redirect
@app.post('/contact')
def contact_submit():
    data = request.form
    logging.info(f"Form received! Name: {data['name']}, Email: {data['email']}")

    send_email(data["name"], data["email"], data["phone"], data["message"])
    logging.info("Email sent successfully.")

    return redirect(url_for('contact_form', success=True))


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
