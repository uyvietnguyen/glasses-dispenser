from flask import Blueprint

page_api = Blueprint('page', __name__,)
@page_api.route("/")
def hello():
    return "YEET ICE YEET!"
