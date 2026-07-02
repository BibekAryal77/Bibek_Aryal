# app.py
# This is the main Flask application file.
# It tells Flask which URLs exist (the "routes") and which HTML page to show for each one.

from flask import Flask, render_template

# Create the Flask application object.
# __name__ tells Flask where to look for templates/ and static/ folders.
app = Flask(__name__)

# --- Data for the Projects page ---
# We keep the project info here as a simple Python list of dictionaries.
# This makes it easy to add/remove a project later without touching the HTML.
projects = [
    {
        "title": "Two-Phase Flow Visualization in Curved Channels",
        "description": (
            "Experimental study of air-water two-phase flow in transparent curved "
            "channels to analyze flow regimes, bubble behavior, void fraction, and "
            "pressure drop."
        ),
        "tools": "High-speed camera, pressure sensors, flow visualization, image processing",
    },
    {
        "title": "CFD Simulation of Flow Boiling in Microchannels",
        "description": (
            "Numerical simulation of bubble dynamics and flow boiling in "
            "microchannels using phase-field, VOF, and level-set approaches."
        ),
        "tools": "COMSOL, ANSYS Fluent, OpenFOAM",
    },
    {
        "title": "Machine Learning for Flow Boiling Heat Transfer Prediction",
        "description": (
            "Development of machine learning models to predict heat transfer "
            "coefficient and pressure drop using experimental datasets and "
            "dimensionless numbers."
        ),
        "tools": "Python, scikit-learn, Random Forest, XGBoost, SHAP, CoolProp",
    },
    {
        "title": "PINN-Based Modeling for Thermal-Fluid Systems",
        "description": (
            "Development of physics-informed neural network models for "
            "thermal-fluid prediction."
        ),
        "tools": "Python, TensorFlow or JAX, PINN modeling",
    },
]

# --- Data for the Research Interests list (used on the About page) ---
research_interests = [
    "Two-phase flow visualization",
    "Flow boiling in microchannels and minichannels",
    "CFD simulation using ANSYS Fluent, COMSOL, and OpenFOAM",
    "Curved channel and U-bend two-phase flow",
    "Heat transfer enhancement",
    "Machine learning for heat transfer coefficient prediction",
    "Physics-informed neural networks",
    "Electronics cooling and thermal management",
]

# --- Data for the Skills page ---
# Each key is a skill category, and each value is a list of specific skills.
skills = {
    "CFD": ["ANSYS Fluent", "COMSOL", "OpenFOAM"],
    "Programming": ["Python", "MATLAB"],
    "Machine Learning": ["scikit-learn", "XGBoost", "SHAP", "TensorFlow/JAX"],
    "Heat Transfer": ["Flow boiling", "Two-phase flow", "Thermal management"],
    "Experimental": [
        "High-speed imaging",
        "Pressure drop measurement",
        "Flow visualization",
    ],
}

# --- Data for the Contact page ---
# Update these links with your real information.
contact_info = {
    "email": "your.email@missouri.edu",
    "linkedin": "https://www.linkedin.com/in/your-profile",
    "scholar": "https://scholar.google.com/citations?user=your-id",
    "github": "https://github.com/your-username",
    "orcid": "https://orcid.org/your-orcid-id",
}


# --- Routes ---
# A "route" connects a URL (like "/") to a Python function that returns a page.

@app.route("/")
def home():
    # Homepage: shows name, title, short intro, and links to other pages.
    return render_template("index.html")


@app.route("/about")
def about():
    # About page: shows the professional summary and research interests list.
    return render_template("about.html", research_interests=research_interests)


@app.route("/projects")
def projects_page():
    # Projects page: loops over the "projects" list above to build project cards.
    return render_template("projects.html", projects=projects)


@app.route("/skills")
def skills_page():
    # Skills page: loops over the "skills" dictionary to build grouped skill lists.
    return render_template("skills.html", skills=skills)


@app.route("/contact")
def contact():
    # Contact page: shows email, LinkedIn, Google Scholar, GitHub, and ORCID links.
    return render_template("contact.html", contact=contact_info)


# This block only runs when you execute "python app.py" directly.
# debug=True auto-reloads the server when you save a file and shows helpful error pages.
if __name__ == "__main__":
    app.run(debug=True)
