from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
from sqlalchemy import update
from models import db


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/businessapp"
print("test")

db.init_app(app)