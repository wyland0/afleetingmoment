import base64,io
from io import BytesIO
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user
from .. import google_client

moments = Blueprint("moments", __name__)

@moments.route("/")
def index():
    moments = []
    # dummies just use all when needed
    for i in range(10):
        moments.append({
            "id": i,
            "description": f"Moment {i}",
        })

    return render_template("index.html", key=google_client.getKey(), moments=moments)

@moments.route("/createmoment", methods=["POST", "GET"])
def create_moment():

    if request.method == "GET":
        return render_template("createmoment.html")
    
    
@moments.route("/comment", methods=["GET"])
def create_comment():
    id = request.args.get('id')

    comments = []
    # dummies just use all when needed
    for i in range(10):
        comments.append({
            "id": i,
            "username": f"User {i}",
            "content": f"Commwadcgjm,l;kmjhngtdrzedscv hbuy7t6edxcghyu7tredghyuent {i}",
            "time": f"2023-10-01 12:00:00",
        })
    return render_template("createcomment.html", id=id, comments=comments)

@moments.route("/comment/<id>", methods=["POST"])
def post_comment():
    return render_template("createcomment.html", id=id)