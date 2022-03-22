from flask import Flask
from flask import Blueprint, Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
import sqlalchemy
from models import Arbeitsgruppe, db


workgroups_blueprint = Blueprint('workgroups_blueprint', __name__)


@workgroups_blueprint.route("/workgroups", methods=["get","post"])
def workgroup():
    session : sqlalchemy.orm.scoping.scoped_session = db.session



    workgroups = session.query(Arbeitsgruppe).all()
    return render_template("workgroups.html", workgroups = workgroups)