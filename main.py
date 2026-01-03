import logging
import os
import smtplib
from datetime import datetime

import requests
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from forms import ContactForm

logging.basicConfig(level=logging.INFO)

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# get all posts
all_posts = requests.get("https://api.npoint.io/abfbbb2fb46d6ccd9494").json()

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6s"
bootstrap = Bootstrap5(app)

def send_email(name, email, phone, message):
    email_message = f"Subject: Flask Blog message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

    logging.info(f"Attempting to send email to {MY_EMAIL}...")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_message)

    logging.info("SMTP connection closed.")

# get and inject current year
@app.context_processor
def inject_now():
    return {"year": datetime.now().year}

#--------------
# Routes
#--------------

@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_form():
    form = ContactForm()
    if form.validate_on_submit():
        logging.info(f"Form Validated! Name: {form.name.data}, Email: {form.email.data}")

        send_email(form.name.data, form.email.data, form.phone.data, form.message.data)
        logging.info("Email sent successfully.")

        return render_template("contact.html", form=form, msg_sent=True)

    return render_template("contact.html", form=form, msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
