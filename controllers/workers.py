from flask import Flask
from flask import Blueprint, Flask, redirect, request, flash, session, render_template
from sqlalchemy import update
import sqlalchemy
from models import db, Mitarbeiter
from forms.AddForms.addWorkersForm import addWorkersForm


workers_blueprint = Blueprint('workers_blueprint', __name__)


@workers_blueprint.route("/workers", methods=["get","post"])
def workers():
    session : sqlalchemy.orm.scoping.scoped_session = db.session



    workers = session.query(Mitarbeiter).all()
    return render_template("workers.html", workers = workers)
@workers_blueprint.route("/addWorkersForm", methods=["get","post"])
def showAddForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    addWorkersFormObject = addWorkersForm()
    print("0")

    if addWorkersFormObject.validate_on_submit():
        print("1")
        
        WorkerObjekt = Mitarbeiter()
        WorkerObjekt.Voname = addWorkersFormObject.Voname.data
        WorkerObjekt.Nachname = addWorkersFormObject.Nachname.data
        WorkerObjekt.Lohn = addWorkersFormObject.Lohn.data
        WorkerObjekt.Adresse = addWorkersFormObject.Adresse.data
        WorkerObjekt.Beschäftigung = addWorkersFormObject.Beschäftigung.data
        WorkerObjekt.Geburtsdatum = addWorkersFormObject.Geburtsdatum.data
        print("2")  
        session.add(WorkerObjekt)
        print("3")
        session.commit()
        print("commited")

        redirect("/")
        print("why?")

    return render_template("addWorkers.html",  form=addWorkersFormObject)