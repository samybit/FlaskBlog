# Flask Simple Blog

A dynamic blogging application built with Python and Flask. This project fetches post content from an external REST API, renders it using Jinja2 templates, and is styled with a modern, responsive CSS design.

The application is fully containerized and deployed live on Railway.

## 🔗 Live Demo

**View the deployed application here:** 👉 [https://web-production-db070.up.railway.app/](https://web-production-db070.up.railway.app/)

## ✨ Features

* **Dynamic Content:** Fetches blog posts in real-time from a remote JSON API (npoint.io) using the `requests` library.
* **Routing:** Implements dynamic URL routing (e.g., `/post/1`) to display individual posts.
* **Templating:** Uses Jinja2 to dynamically render HTML titles, subtitles, and body content.
* **Responsive Design:** Custom CSS styling with a modern color palette, card-based layout, and hover effects.
* **Production Ready:** Configured with Gunicorn for stable deployment on cloud platforms.

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Templating:** Jinja2
* **API Handling:** Requests Library
* **Styling:** Custom CSS3
* **Deployment:** Railway, Gunicorn (WSGI Server)

## 💡 Key Learnings & Technical Skills

This project served as a comprehensive exercise in full-stack web development. Key skills demonstrated include:

* **Deployment Workflow:** Successfully managed the lifecycle of a dynamic app by deploying to **Railway**, moving beyond local development.
* **Server Configuration:** Configured a production environment using a **`Procfile`** to manage startup commands and **Gunicorn** as the WSGI server.
* **Dependency Management:** Learned to maintain a clean build environment by stripping `requirements.txt` down to essential packages (`Flask`, `requests`, `gunicorn`).
* **External API Integration:** Decoupled data from the application logic by fetching JSON data remotely, simulating a real-world CMS integration.
* **Dynamic Routing & Templating:** Mastered Flask's variable rules (`<int:index>`) and Jinja2 loops to generate content programmatically.

## 🚀 How to Run Locally

If you want to run this project on your own machine:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/samybit/FlaskBlog.git](https://github.com/samybit/FlaskBlog.git)
    cd FlaskBlog
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python main.py
    ```

4.  **Open in Browser**
    Visit `http://127.0.0.1:5000/` to see the app running.

## 📂 Project Structure

```text
.
|-- main.py              # Application entry point and route definitions
|-- post.py              # Class definition for Post objects
|-- templates/
|   |-- index.html       # Homepage template
|   |-- post.html        # Single post view template
|-- static/
|   |-- css/
|       |-- styles.css   # Global styles
|-- Procfile             # Startup command for Railway/Render
|-- requirements.txt     # List of python dependencies
|-- README.md            # Project documentation
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
