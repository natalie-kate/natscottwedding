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
    return render_template('wedding_diary.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/rsvp")
def rsvp():
    return render_template('rsvp.html')


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    """ add_book view to add book to library """
    # if add_book form submitted get information from form
    if request.method == "POST":
        # If title stripped of spaces is empty then display
        # flash message and reload add_book form
        if not request.form.get("title").strip():
            flash("Please provide a title")
            return redirect(url_for('add_book'))
        # If title supplied then get information from form
        else:
            is_series = "Yes" if request.form.get("series") else "No"
            # Check if book already exists in database
            existing_book = mongo.db.books.find_one(
                {"title": request.form.get("title").lower()}
            )
            # If book exists, display message and reload add_book
            if existing_book:
                flash("This book is already in our Library")
                return redirect(url_for("add_book"))
            # Insert new book, display message and redirect to library
            else:
                title = request.form.get("title")
                book = {
                    "title": title.lower(),
                    "author": request.form.get("author").lower(),
                    "synopsis": request.form.get("synopsis"),
                    "series": is_series,
                    "series_name": request.form.get("series_name").lower(),
                    "genre": request.form.get("genre"),
                    "cover_image": request.form.get("cover_image"),
                    "rating": int(request.form.get("rating")),
                    "review": request.form.get("review"),
                    "added_by": session["user"]
                    }
                mongo.db.books.insert_one(book)
                flash(
                    "Thankyou for contributing to the library," +
                    f' {title.title()} has now been added')
                return redirect(url_for("library"))
    # Use add_book template, passing in admin and genre
    if "user" in session:
        return render_template("add-book.html", genres=genres(), admin=admin())
    else:
        flash("You need to be signed in to do that")
        return redirect(url_for("sign_in"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
