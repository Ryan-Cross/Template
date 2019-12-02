# this module tells NGINX what files are what as it serves HTML and CSS

# first it needs the central flask object
from TEMPLATEapp import app

# Then it needs whatever tooling you plan to run from the Flask module
from flask import render_template, url_for, request, flash

# now from here down we are directing traffic for NGINX

@app.route('/')
def index():
    return render_template("MarkUpBaby.html")

