# freeze.py
# GitHub Pages can only serve plain HTML/CSS/JS files - it cannot run a Python
# server. This script uses Frozen-Flask to "freeze" every page of app.py into
# real .html files inside the docs/ folder, which GitHub Pages then serves.
#
# Run it with:
#     venv\Scripts\python freeze.py
# Then commit and push the docs/ folder to GitHub.

from pathlib import Path

from flask_frozen import Freezer
from app import app

# Save the generated site into docs/, since GitHub Pages can be configured
# to publish straight from a repo's /docs folder.
app.config["FREEZER_DESTINATION"] = "docs"

# Use relative links (e.g. "../about/") instead of absolute ones (e.g. "/about/").
# This makes the site work whether it's hosted at the root of a domain or in a
# subfolder, like https://bibekaryal77.github.io/Personal-Website/.
app.config["FREEZER_RELATIVE_URLS"] = True

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()

    # Tell GitHub Pages to skip Jekyll processing and serve the files as-is.
    # Frozen-Flask doesn't know about this file, so we recreate it every run.
    (Path(app.config["FREEZER_DESTINATION"]) / ".nojekyll").touch()

    print("Static site generated in the docs/ folder.")
