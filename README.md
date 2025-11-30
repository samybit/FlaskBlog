# My Simple Flask Blog

A basic blogging platform built with Flask, Jinja2 templating, and static CSS. The blog pulls post data from a remote JSON API.

## Features

* **Homepage:** Displays a list of all available blog posts with titles and subtitles.
* **Individual Post View:** Allows users to click "Read" to view the full content of a specific post.
* **External Data Source:** Uses the `requests` library to fetch blog data from `https://api.npoint.io/c790b4d5cab58020d391`.

## How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_REPO_URL]
    cd my-simple-flask-blog
    ```
2.  **Install Dependencies:**
    ```bash
    pip install Flask requests
    ```
3.  **Run the Application:**
    ```bash
    python main.py
    ```
4.  **Access:** Open your browser and navigate to `http://127.0.0.1:5000/`.
