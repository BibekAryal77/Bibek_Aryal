# Bibek Aryal — Personal Academic Portfolio Website

A simple personal portfolio website built with **Python (Flask)**, **HTML**, and **CSS**.
No React, no databases, no login — just a clean beginner-friendly Flask app.

## Folder structure

```
personal_website/
│
├── app.py                 # Main Flask app: routes + page data
├── requirements.txt        # Python packages needed (just Flask)
├── README.md                # This file
│
├── static/
│   ├── css/
│   │   └── style.css       # All styling for the site
│   └── images/
│       └── profile.jpg     # Your profile picture
│
└── templates/
    ├── base.html            # Shared layout (navbar, footer) used by every page
    ├── index.html           # Home page
    ├── about.html           # About page
    ├── projects.html        # Projects page
    ├── skills.html          # Skills page
    └── contact.html         # Contact page
```

## How to run it locally (Windows PowerShell)

1. Open PowerShell and go to the `personal_website` folder.
2. Create a virtual environment (a private, isolated copy of Python for this project):
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```
   You should see `(venv)` appear at the start of your PowerShell prompt.
4. Install the required packages (just Flask):
   ```
   pip install -r requirements.txt
   ```
5. Run the website:
   ```
   python app.py
   ```
6. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

To stop the server, go back to PowerShell and press `Ctrl + C`.

Next time you want to run the site, you only need steps 3, 5, and 6
(the virtual environment and packages are already set up).

## How everything works

### 1. What each file does
- **app.py** — The heart of the app. It creates the Flask app, stores your project/skill/contact
  data in Python lists and dictionaries, and defines a "route" (URL) for each page.
- **templates/*.html** — The HTML pages. Flask uses a template engine called **Jinja2** to fill
  these HTML files with data from `app.py` (like `{{ project.title }}`).
- **static/css/style.css** — The single stylesheet controlling colors, spacing, fonts, and the
  mobile-friendly layout for the whole site.
- **static/images/profile.jpg** — Your photo, shown on the Home page.

### 2. What Flask is doing in app.py
- `app = Flask(__name__)` creates the web application.
- `@app.route("/about")` is a **decorator** that says "when someone visits `/about` in their
  browser, run the function right below it."
- Each route function calls `render_template("about.html", ...)`, which finds the HTML file in
  `templates/` and sends it to the browser, optionally passing in Python data (like the
  `research_interests` list) that the HTML can display.

### 3. How HTML templates work
- Every page (`index.html`, `about.html`, etc.) starts with `{% extends "base.html" %}`. This
  means "use base.html as the outer layout, and insert my content into it."
- `base.html` has a `{% block content %}{% endblock %}` — this is the empty slot that each page
  fills in with `{% block content %} ... {% endblock %}`.
- `{{ variable_name }}` prints a Python value into the HTML (e.g. `{{ project.title }}`).
- `{% for item in list %} ... {% endfor %}` repeats HTML for every item in a Python list —
  this is how the Projects and Skills pages build their cards without copy-pasting HTML.

### 4. How CSS is connected to the website
- `base.html` contains this line in the `<head>`:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  ```
- `url_for('static', filename=...)` tells Flask "build the correct URL to a file inside the
  `static/` folder." Since every page extends `base.html`, every page automatically loads
  `style.css`.

### 5. How to add a new page
1. Create a new HTML file in `templates/`, e.g. `templates/publications.html`:
   ```html
   {% extends "base.html" %}
   {% block title %}Publications | Bibek Aryal{% endblock %}
   {% block content %}
   <section class="page-section">
       <h1>Publications</h1>
       <p>List your publications here.</p>
   </section>
   {% endblock %}
   ```
2. Add a route in `app.py`:
   ```python
   @app.route("/publications")
   def publications():
       return render_template("publications.html")
   ```
3. Add a link in the navbar inside `templates/base.html`:
   ```html
   <a href="{{ url_for('publications') }}">Publications</a>
   ```

### 6. How to add a new project
Open `app.py` and add a new dictionary to the `projects` list:
```python
{
    "title": "Your New Project Title",
    "description": "A short description of the project.",
    "tools": "List the tools/software you used",
},
```
The Projects page automatically shows it — no HTML editing needed, because `projects.html`
loops over the `projects` list.

### 7. How to update your LinkedIn, Google Scholar, GitHub, and email links
Open `app.py` and edit the `contact_info` dictionary near the top:
```python
contact_info = {
    "email": "your.email@missouri.edu",
    "linkedin": "https://www.linkedin.com/in/your-profile",
    "scholar": "https://scholar.google.com/citations?user=your-id",
    "github": "https://github.com/your-username",
    "orcid": "https://orcid.org/your-orcid-id",
}
```
Save the file and refresh the page in your browser.

### 8. How to add your profile picture
Replace the file at `static/images/profile.jpg` with your own photo, keeping the same file
name (`profile.jpg`). If you want to use a different name or format (like `.png`), update the
filename in `templates/index.html`:
```html
<img src="{{ url_for('static', filename='images/profile.jpg') }}" ...>
```

### 9. How to run the website locally
See the **"How to run it locally"** section above.

## What's next?
This is intentionally a simple, beginner-level version. Once you're comfortable with how it
works, you can ask to upgrade it step by step — for example: a contact form, a blog/publications
section, deployment to a live server, or a database for dynamic content.
