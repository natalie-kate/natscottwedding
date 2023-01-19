"""Imports used to connect with and use MongoDB,use flask templates and
pagination and werkzeug for password security"""
import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_paginate import Pagination, get_page_args
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# configurations
app = Flask(__name__)
# app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# app.secret_key = os.environ.get("SECRET_KEY")
# mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/story")
def story():
    return render_template('our_story.html')


@app.route("/day")
def day():
    return render_template('our_day.html')


@app.route("/diary")
def diary():
    return render_template('wedding_diaries.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/rsvp")
def rsvp():
    return render_template('rsvp.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
