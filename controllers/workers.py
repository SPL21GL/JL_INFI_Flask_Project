from flask import Flask
from flask import Blueprint, Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
import sqlalchemy
from models import db, Mitarbeiter


workers_blueprint = Blueprint('workers_blueprint', __name__)


@workers_blueprint.route("/workers", methods=["get","post"])
def workers():
    session : sqlalchemy.orm.scoping.scoped_session = db.session



    workers = session.query(Mitarbeiter).all()
    return render_template("workers.html", workers = workers)