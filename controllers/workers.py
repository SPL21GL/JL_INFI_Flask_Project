from flask import Flask
from flask import Blueprint, Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
import sqlalchemy
from models import db, Mitarbeiter


#from models import db  verfollständigen

workers_blueprint = Blueprint('workers_blueprint', __name__)


@workers_blueprint.route("/workers", methods=["get","post"])
def workers():
    session : sqlalchemy.orm.scoping.scoped_session = db.session


    workers = session.query(Mitarbeiter).all() #[1,2,3,4,5]
    return render_template("workers.html", worker = workers)