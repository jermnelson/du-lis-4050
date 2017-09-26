__author__ = "Jeremy Nelson"

from flask import abort, Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config["FLATPAGES_EXTENSION"] = ".md"
pages = FlatPages(app)

@app.route("/<path:name>")
def display(name):
    page = pages.get_or_404(name)
    return render_template("du-lis-4050/page.html",
                           page=page)

@app.route("/")
def home():
    return render_template("du-lis-4050/index.html", pages=pages)
