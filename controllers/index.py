from flask import Flask
from flask import Blueprint, Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
import sqlalchemy


#from models import db  verfollständigen

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route("/",methods=["get","post"])


def index():
    #session : sqlalchemy.orm.scoping.scoped_session = db.session
    return render_template("index.html")