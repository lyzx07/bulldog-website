import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from flask_mail import Mail, Message

#####STILL WORKING ON THIS PROJECT!! NOT COMPLETE!!#####

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

conn = sqlite3.connect('puppies.db', check_same_thread=False)
c = conn.cursor()

password = os.environ.get('my_password')

# Check if environment variable is set
if password is None:
    print('Environment variable not set!')
else:
    print('Environment variable is set!')


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lyzx07@yahoo.com'
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

    
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

@app.route('/send_email', methods=["POST"])
def send_email():
    try:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        visitor_email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        zip = request.form.get("zip")
        message = request.form.get("message")

        msg = Message('Hello', sender = 'lyzx07@yahoo.com', recipients = ['lyzx07@yahoo.com'])
        msg.body = f"This is the email body \n Name: {fname} {lname} \n Email: {visitor_email} \n Phone: {phone} \n Address: {address}, {city}, {state}, {zip} \n Message: {message}"
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return(str(e))
