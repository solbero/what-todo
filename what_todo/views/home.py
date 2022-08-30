from flask import Blueprint, render_template

route = Blueprint("home", __name__)


@route.get("/")
def index():
    return render_template("home.j2")
