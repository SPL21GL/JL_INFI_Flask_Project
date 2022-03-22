from flask import Flask
from flask import Blueprint, Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
import sqlalchemy
from models import db, Abteilung


#from models import db  verfollständigen

compartments_blueprint = Blueprint('compartments_blueprint', __name__)


@compartments_blueprint.route("/compartments", methods=["get","post"])
def compartment():
    session : sqlalchemy.orm.scoping.scoped_session = db.session



    compartments = session.query(Abteilung).all()
    return render_template("compartments.html", compartments = compartments)