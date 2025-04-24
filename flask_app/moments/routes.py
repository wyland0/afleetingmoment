import base64,io
from io import BytesIO
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user
from .. import google_client

moments = Blueprint("moments", __name__)

@moments.route("/")
def index():

    moments = []

    # dummies
    for i in range(10):
        moments.append({
            "id": i,
            "description": f"Moment {i}",
        })

    return render_template("index.html", key=google_client.getKey(), moments=moments)