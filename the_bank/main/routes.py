"""Import libraries."""
from flask import render_template, Blueprint

main = Blueprint("main", __name__)

# Here we are serving a simply static html page with flask. There are no other
# routes that return templates. You can even look in the templates folder and
# see that we only have "home.html.j2". Keep this in mind as we build out the
# app. There is only ever one template which is then changed on the front-end


@main.route("/")
def home():
    """Return home template."""
    return render_template("home.html.j2")


# TODO: go to the-bank/api/routes.py
