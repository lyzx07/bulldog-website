import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp

#####STILL WORKING ON THIS PROJECT!! NOT COMPLETE!!#####

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

conn = sqlite3.connect('puppies.db', check_same_thread=False)
c = conn.cursor()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")


@app.route("/puppies", methods=["GET", "POST"])
def puppies():
    return render_template("puppies.html")


@app.route("/parents", methods=["GET", "POST"])
def parents():
    parent = c.execute(
        "SELECT name, gender, year_born, litters_had FROM parents")
    result = c.fetchall()

    return render_template("parents.html", result=result)


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")
