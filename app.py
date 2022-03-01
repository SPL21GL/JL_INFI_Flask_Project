from flask import Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
from models import db


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/businessapp"

db.init_app(app)
app.secret_key = "VerSecretSecretKey"

@app.route("/", methods=["get","post"])

#Show Hello World on index page
def index():
    return render_template("index.html")
app.run(debug=True)