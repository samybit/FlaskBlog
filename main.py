from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import datetime

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


# contact GET
@app.get('/contact')
def contact_form():
    # check if message has been sent -> if the URL has "?success=True"
    msg_sent = request.args.get('success')

    # Pass status to the HTML
    return render_template("contact.html", msg_sent=msg_sent)

# contact POST
@app.post('/contact')
def contact_submit():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
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
