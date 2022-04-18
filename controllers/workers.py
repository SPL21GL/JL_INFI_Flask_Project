from flask import Flask
from flask import Blueprint, Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
import sqlalchemy
from models import db, Mitarbeiter
from forms.AddForms.addWorkersForm import addWorkersForm

ROWS_PER_PAGE = 5
workers_blueprint = Blueprint('workers_blueprint', __name__)


@workers_blueprint.route("/workers", methods=["get","post"])
def show_workers():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    page = request.args.get('page', 1, type=int)
    workers = session.query(Mitarbeiter).order_by(Mitarbeiter.MitarbeiterID).paginate(page, ROWS_PER_PAGE, error_out=False)

    return render_template("workers.html", paginator=workers)


@workers_blueprint.route("/addWorkersForm", methods=["get","post"])
def showAddForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    addWorkersFormObject = addWorkersForm()

    if addWorkersFormObject.validate_on_submit():
        
        WorkerObjekt = Mitarbeiter()
        WorkerObjekt.Voname = addWorkersFormObject.Voname.data
        WorkerObjekt.Nachname = addWorkersFormObject.Nachname.data
        WorkerObjekt.Lohn = addWorkersFormObject.Lohn.data
        WorkerObjekt.Adresse = addWorkersFormObject.Adresse.data
        WorkerObjekt.Beschäftigung = addWorkersFormObject.Beschäftigung.data
        WorkerObjekt.Geburtsdatum = addWorkersFormObject.Geburtsdatum.data
        session.add(WorkerObjekt)
        session.commit()

        redirect("/")


    return render_template("addWorkers.html",  form=addWorkersFormObject)

@workers_blueprint.route("/editWorkersForm", methods=["get","post"])
def submit_edit_workers():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
