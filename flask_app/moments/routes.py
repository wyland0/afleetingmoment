import base64,io
from io import BytesIO
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user

moments = Blueprint("moments", __name__)

@moments.route("/")
def index():
    return render_template("index.html")