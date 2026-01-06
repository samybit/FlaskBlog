# Flask Simple Blog

A dynamic blogging application built with Python and Flask. This project fetches post content from an external REST API, renders it using Jinja2 templates, and is styled with a modern, responsive CSS design.

## 🔗 Live Demo

**View the deployed application here:** 👉 [https://web-production-db070.up.railway.app/](https://web-production-db070.up.railway.app/)

## ✨ Key Refactored Features

* **Professional Form Handling:** Integrated **Flask-WTF** for secure, object-oriented form management, replacing standard HTML forms with validated Python classes.
* **Jinja2 Template Inheritance:** Optimized the frontend architecture by moving from simple "includes" to a robust **Master Layout (`base.html`)** system with custom blocks.
* **Custom UI Macros:** Developed reusable Jinja2 macros to render **Bootstrap 5 Floating Labels** with automated validation error feedback.
* **Persistent Background Audio:** Engineered a "Web 1.0 vibe" background music player that persists across page reloads using **JavaScript LocalStorage** and a dedicated **Python Streaming Route** to bypass browser autoplay and caching restrictions.
* **Responsive UX Design:** Enhanced the navigation bar for high-contrast visibility on mobile devices, ensuring accessibility across all viewports.

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Flask, **Flask-WTF**, **Bootstrap-Flask**
* **Frontend:** HTML5, CSS3, JavaScript (Bootstrap 5, FontAwesome)
* **Templating:** Jinja2 (Inheritance & Macros)
* **API/Data:** RESTful JSON API integration via `requests`
* **Environment:** `python-dotenv` for secret management
* **Deployment:** Railway (Gunicorn WSGI)

## 💡 Key Learnings & Technical Skills

This project demonstrates a transition from basic web development to professional full-stack engineering:

* **Object-Oriented Web Forms:** Implementing CSRF protection and server-side validation logic.
* **Streaming Content Delivery:** Configured custom Flask routes and MIME-type handling to serve audio streams correctly across different browsers.
* **State Management:** Using browser storage to maintain a seamless user experience during a stateless HTTP session (page transitions).
* **Refactoring Mastery:** Successfully restructured a functional app to improve maintainability, security, and scalability.

## 🚀 How to Run Locally

If you want to run this project on your own machine:

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/samybit/FlaskBlog.git
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
|-- main.py              # Application entry point, routes, and context processors
|-- forms.py             # WTForms classes for secure user input
|-- pyproject.toml       # Ruff linter & formatter configuration
|-- templates/           # HTML Templates (Jinja2)
|   |-- base.html        # Master layout (Navbar, Footer, JS Scripts)
|   |-- index.html       # Home page (loops through posts)
|   |-- post.html        # Individual post page (dynamic content)
|   |-- about.html       # Static about page
|   |-- contact.html     # Contact form page
|-- static/              # Static Assets
|   |-- css/
|       |-- styles.css   # Bootstrap & Custom styles
|   |-- js/
|       |-- scripts.js   # Theme interactions
|   |-- assets/          # Background MP3 & Favicon
|-- .env                 # Environment variables (API keys & secrets)
|-- .gitignore           # Specifies files to exclude from Git
|-- Procfile             # Production startup command (Gunicorn)
|-- requirements.txt     # Python dependencies
|-- LICENSE              # Project License
|-- README.md            # Project documentation
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
